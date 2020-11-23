__all__ = ["api_browse"]

import pprint

from ..common import config
from ..metadata import meta_types
from ..elastic import elastic, QueryBuilder
from ..objects import Asset

from .responses import response


class BrowserHelper():
    def __init__(self):
        self._fulltext_fields = None

    def load_fulltext_fields(self):
        self._fulltext_fields = []
        for key in config["meta_types"]:
            ft_priority = config["meta_types"][key].get("fulltext")
            if not ft_priority:
                continue
            self._fulltext_fields.append(f"{key}^{ft_priority}")

    @property
    def fulltext_fields(self):
        if self._fulltext_fields is None:
            self.load_fulltext_fields()
        return self._fulltext_fields

browser_helper = BrowserHelper()


async def api_browse(**kwargs):
    try:
        id_view = int(kwargs.get("v", 0))
        if id_view == 0:
            id_view = min(config.get("views", [-1]))
    except ValueError:
        return response(400, "id_view must be an integer")

    try:
        page = max(1, int(kwargs.get("p", 1)))
    except ValueError:
        return response(400, "p must be an integer")

    try:
        records_per_page = int(kwargs.get("l", 20))
    except ValueError:
        return response(400, "l must be an integer")


    qb = QueryBuilder()
    if kwargs.get("q"):
        qb.must({
            "simple_query_string": {
                "query": kwargs.get("q"),
                "default_operator" : "and",
                "fields": browser_helper.fulltext_fields,
                "fuzzy_max_expansions" : 0
            }
        })


    if id_view > 0:
        view_config = config["views"].get(id_view)
        if not id_view:
            return response(400, "No such view {}".format(id_view))

        result_keys = view_config["fields"]
        qb.from_view_config(view_config.get("search", {}))
    else:
        result_keys = ["id"]


    searchconfig = {
        "index" : "assets",
        "body" : {
                "query": qb.build(),
                "size" : records_per_page,
                "from" : (page-1)*records_per_page
            }
        }


    data = await elastic.search(**searchconfig)
    pprint.pprint(data)
    hits = data["hits"]["hits"]
    max_score = data["hits"]["max_score"]
    if not max_score:
        try:
            result_keys.remove("_score")
        except ValueError:
            pass

    count = data["hits"]["total"]["value"]

    data = []
    for hit in hits:
        row = {}
        asset = Asset(**hit["_source"])
        

        for key in result_keys:
            if key.startswith("_"):
                continue
            row[key] = asset.show(key, mode="listing") 


        row["_id"] = asset["id"]
        status = asset["status"]

        if status == 0:
            row["_class"] = "item-offline"
        elif status == 3:
            row["_class"] = "item-trashed"
        elif status == 4:
            row["_class"] = "item-archived"
        else:
            row["_class"] = ""

        if max_score:
            row["_score"] = "{:.01f}%".format(hit["_score"]/max_score*100)
        data.append(row)

    result = {
        "id_view" : id_view,
        "count" : count,
        "data" : data,
    }

    if "keyinfo" in kwargs:
        keyinfo = []
        for key in result_keys:

            v = {
                "key" : key,
                "display" : meta_types[key].get_alias("en"),
                "class" : "" if key in ["title", "subtitle"] else "min"
            }
            keyinfo.append(v)
        result["keys"] = keyinfo


    return response(200, **result)
