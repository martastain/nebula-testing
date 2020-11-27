__all__ = ["cache"]

"""
TODO:
    - Exceptions handling
"""

import json
import asyncio

from .common import *

if config.get("async"):
    import aioredis
else:
    import redis

class Cache():
    def __init__(self, use_async=False):
        logging.info("Starting cache. Async", use_async)
        self.use_async = use_async
        self.redis_url = config["redis"]
        self.redis = None

    def __getattr__(self, attr):
        if self.use_async:
            return getattr(self, "async_"+attr)
        return getattr(self, "sync_"+attr)


    def sync_get(self, namespace, id):
        if not self.redis:
            pool = redis.ConnectionPool.from_url(config["redis"])
            self.redis = redis.Redis(connection_pool=pool) 
        key = f"{namespace}-{id}"
        value = self.redis.get(key)
        return json.loads(value)

    def sync_set(self, namespace, id, value):
        if not self.redis:
            pool = redis.ConnectionPool.from_url(config["redis"])
            self.redis = redis.Redis(connection_pool=pool) 
        key = f"{namespace}-{id}"
        self.redis.set(key, json.dumps(value))


    async def async_get(self, namespace, id):
        if not self.redis:
            self.redis = await aioredis.create_redis_pool(self.redis_url)
        key = f"{namespace}-{id}"
        value = await self.redis.get(key)
        return json.loads(value)

    async def async_set(self, namespace, id, value):
        if not self.redis:
            self.redis = await aioredis.create_redis_pool(self.redis_url)
        key = f"{namespace}-{id}"
        await self.redis.set(key, json.dumps(value))

    async def async_close(self):
        if self.redis:
            await self.redis.close()
            await self.redis.wait_closed()

    def __del__(self):
        if self.use_async:
            asyncio.shield(self.async_close())
        else:
            self.redis.close()


cache = Cache(config.get("async"))
