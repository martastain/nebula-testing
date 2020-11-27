#!/usr/bin/env python3

import json
import halo

from nebula.common import *
from nebula.elastic import elastic
from nebula.cache import cache
from nebula.metadata import meta_types
from nebula.objects import asset_factory

print("\n")

es_settings = {
    "analysis": {
        "analyzer": {
            "default": {
                "type": "custom",
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "asciifolding"
                ]
            }
        }
    }
}


CLASS_TO_ES_TYPE = {
    STRING :   {"type": "text"},
    TEXT :     {"type": "text"},
    INTEGER :  {"type": "long"},
    NUMERIC :  {"type": "float"},
    BOOLEAN :  {"type": "boolean"},
    DATETIME : {"type": "date", "format" : "epoch_second"},
    TIMECODE : {"type": "float"},
    OBJECT :   {"type": "object"},
    FRACTION : {"type": "float"},
    SELECT :   {"type": "text"},
    LIST :     {"type": "text"},
    COLOR :    {"type": "integer"},
}


def prepare():
    spinner = halo.Halo(text="Connecting to Elastic search", spinner="dots")
    spinner.start()

    properties = {}
    for key in meta_types.keys():
        meta_type = meta_types[key]
        if not meta_type["index"]:
            continue
        properties[key] = CLASS_TO_ES_TYPE[meta_type["class"]]
        

    spinner.text = "Deleting old index"
    elastic.indices.delete(index="assets", ignore=[404])

    spinner.text = "Installing new index"
    elastic.indices.create(
        index="assets", 
        body={
            "settings" : es_settings,
            "mappings" : {
                "properties" : properties
            }
        }
    )
    spinner.succeed(text="Elastic search configured")










def store():
    spinner = halo.Halo(text="Loading data...", spinner="dots")
    spinner.start()
    data = json.load(open("/data/import/assets.json"))
    spinner.succeed("Data loaded")

    spinner = halo.Halo(text="Importing", spinner="dots")
    spinner.start()
    total = len(data)
    for i, meta in enumerate(data):
        aid = meta["id"]
        spinner.text = "Inserting asset {} of {} (ID {}) ".format(i, total, aid)

        asset = asset_factory(meta)

        elastic.index(index='assets', id=aid, body=asset.meta)
        cache.set("asset", aid, json.dumps(asset.meta))

    spinner.succeed("Inserted {} assets".format(total))



store()