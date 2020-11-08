__all__ = ["api", "response", "raw_response"]

from .cache import cache
from .search import search


class API():
    async def suggest(self, query:str="") -> list:
        if query:
            es_query = {
                "bool" : {"must":{
                "simple_query_string": {
                    "query": query,
                    "default_operator" : "and",
                    "fields": ["title^3", "subtitle^2", "keywords", "description", "id/main"],
                    "fuzzy_max_expansions" : 0
                }
                }}
            }
        else:
            es_query = {"match_all" : {}}

        d = await search.query(
            index="assets",
            body={
                "query":es_query,
                },
            size=20
        )
        hits = d["hits"]["hits"]
        result = [
            {
                "id" : h["_id"],
                "idec" : h["_source"].get("id/main"),
                "title" : h["_source"].get("title"),
                "subtitle" : h["_source"].get("subtitle")
            } for h in hits
        ]
        return {"data":result}



api = API()
