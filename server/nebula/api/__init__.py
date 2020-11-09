__all__ = ["api"]

from .browse import api_browse

class API():
    async def browse(self, id_view:int=0, query:str="") -> list:
        if not id_view:
            pass #TODO: default_view
        #es_query = build_es_query(id_view, query)

        if query:
            es_query = {
                "bool" : {
                    "must":{
                        "simple_query_string": {
                            "query": query,
                            "default_operator" : "and",
                            "fields": ["title^3", "subtitle^2", "keywords", "description", "id/main"],
                            "fuzzy_max_expansions" : 0
                        }
                    },

                    "filter":{
                        "match" : {
                            "id_folder" : 2,
                        }
                    }
                }
            }
        else:
            es_query = {"match_all" : {}}

        d = await api_browse(
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
