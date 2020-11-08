__all__ = ["cache"]

"""
TODO:
    - Exceptions handling
"""

import json
import asyncio
import aioredis

from .common import *


def require_redis(func):
    async def redis_decorator(self, *args, **kwargs):
        print ("Connecting to redis")
        if self.redis is None:
            self.redis = await aioredis.create_redis_pool(self.redis_url)
        return await func(self, *args, **kwargs)
    return redis_decorator


class Cache():
    def __init__(self):
        self.redis_url = config["redis"]
        self.redis = None

    @require_redis
    async def get(self, namespace, key):
        key = f"{namespace}-{id}"
        value = await self.redis.get(key)
        return json.load(value)

    @require_redis
    async def set(self, namespace, key, value):
        key = f"{namespace}-{id}"
        await self.redis.set(key, json.dumps(value))

    def __del__(self):
        if self.redis:
            self.redis.close()
            asyncio.shield(self.redis.wait_closed())


cache = Cache()
