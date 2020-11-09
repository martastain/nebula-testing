__all__ = ["api_browse"]

import asyncio
import elasticsearch

from ..common import *

from .responses import *

class Elastic():
    def __init__(self):
        self.es = None

    async def query(self, **kwargs):
        """Run elasticsearch "search" query with given arguments"""
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


elastic = Elastic()
async def api_browse(**kwargs):
     return await elastic.query(**kwargs)
