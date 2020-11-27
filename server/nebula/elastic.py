__all__ = ["elastic", "QueryBuilder"]

import asyncio
import elasticsearch

from .common import *

class QueryBuilder():
    def __init__(self):
        self.e_must = []
        self.e_filter = []
        self.e_should = []
        self.e_must_not = []

    def from_view_config(self, data):
        for f in data.get("filter", []):
            self.filter(f)
        for m in data.get("must", []):
            self.must(m)
        for s in data.get("should", []):
            self.should(s)
        for n in data.get("must_not", []):
            self.must_not(n)

    def must(self, cond):
        self.e_must.append(cond)

    def filter(self, cond):
        self.e_filter.append(cond)

    def should(self, cond):
        self.e_should.append(cond)

    def must_not(self, cond):
        self.e_must_not.append(cond)

    def build(self):
        r = {}
        if self.e_must:
            r["must"] = self.e_must
        if self.e_filter:
            r["filter"] = self.e_filter
        if self.e_should:
            r["should"] = self.e_should
        if self.e_must_not:
            r["must_not"] = self.e_must_not
        if not r:
            return {"match_all" : {}}
        return {"bool" : r}


class Elastic():
    def __init__(self, use_async=False):
        logging.info("Starting elastic. Async", use_async)
        self.use_async = use_async
        self.es = None

    def connect(self):
        if self.use_async:
            self.es = elasticsearch.AsyncElasticsearch(config["elastic"])
        else:
            self.es = elasticsearch.Elasticsearch(config["elastic"])

    def __getattr__(self, attr):
        if not self.es:
            self.connect()
        return getattr(self.es, attr)
        

    async def async_close(self):
        if self.es:
            await self.es.close()
            self.es = None

    def __del__(self):
        if self.es:
            if self.use_async:
                asyncio.shield(self.async_close())
            else:
                self.es.close()






elastic = Elastic(config.get("async"))
