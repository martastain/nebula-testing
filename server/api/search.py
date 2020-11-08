__all__ = ["search"]

import asyncio
import elasticsearch

from .common import *

class Search():
    def __init__(self):
        self.es = None

    async def query(self, **kwargs):
        if not self.es:
            self.es = elasticsearch.AsyncElasticsearch(config["elastic"])
        response = await self.es.search(**kwargs)
        return response

    async def close(self):
        await self.es.close()
        self.es = None

    def __del__(self):
        if self.es:
            asyncio.shield(self.close())

search = Search()
