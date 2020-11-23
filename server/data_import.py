#!/usr/bin/env python3
import sys
import json
import halo
import asyncio
import aioredis

from nebula.elastic import elastic
from nebula.constants.meta_classes import *
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


async def prepare():
    spinner = halo.Halo(text="Connecting to Elastic search", spinner="dots")
    spinner.start()

    properties = {}
    for key in meta_types.keys():
        meta_type = meta_types[key]
        if not meta_type["index"]:
            continue
        properties[key] = CLASS_TO_ES_TYPE[meta_type["class"]]
        

    spinner.text = "Deleting old index"
    await elastic.es.indices.delete(index="assets", ignore=[404])

    spinner.text = "Installing new index"
    await elastic.es.indices.create(
        index="assets", 
        body={
            "settings" : es_settings,
            "mappings" : {
                "properties" : properties
            }
        }
    )
    spinner.succeed(text="Elastic search configured")







spinner = halo.Halo(text="Loading data...", spinner="dots")
spinner.start()
data = json.load(open("/data/import/assets.json"))
spinner.succeed("Data loaded")


async def get_redis():
    return await aioredis.create_redis_pool('redis://redis')


async def store():
    redis = await get_redis()
    spinner = halo.Halo(text="Validating records", spinner="dots")
    spinner.start()
    total = len(data)
    for i, meta in enumerate(data):
        aid = meta["id"]
        spinner.text = "Inserting asset {} of {} (ID {}) ".format(i, total, aid)

        asset = asset_factory(meta)

        await elastic.es.index(index='assets', id=aid, body=asset.meta)
        await redis.set("asset" + str(aid), json.dumps(asset.meta))

    redis.close()
    await redis.wait_closed()
    spinner.succeed("Inserted {} assets".format(total))










async def validate_records():
    spinner = halo.Halo(text="Validating records", spinner="dots")
    spinner.start()
    redis = await get_redis()
    total = len(data)
    for i, meta in enumerate(data):
        spinner.text = "Validating asset ID {} of {} (ID {})".format(i, total, meta["id"])
        val = await redis.get("asset" + str(meta["id"]))
        val = json.loads(val)

        if val != meta:
            spinner.stop()
            print("ERROR")
            print (val)
            print ()
            print (meta)
            break
    else:
        spinner.stop()
    redis.close()
    await redis.wait_closed()
    spinner.succeed("Validated {} assets".format(total))




loop = asyncio.get_event_loop()
try:
    elastic.connect()
    loop.run_until_complete(prepare())
    loop.run_until_complete(store())
#asyncio.run(validate_records())
    loop.run_until_complete(elastic.close())
finally:
    loop.close()