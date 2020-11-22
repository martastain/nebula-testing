#!/usr/bin/env python3
from nebula.objects import safe_get_asset
import sys
import json
import halo
import asyncio
import aioredis

from nebula.elastic import elastic
from nebula.constants.meta_classes import *
from nebula.metadata import meta_types
from nebula.objects import safe_get_asset

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
    STRING : "text",
    TEXT : "text",
    INTEGER : "integer",
    NUMERIC : "float",
    BOOLEAN : "boolean",
    DATETIME : "date",
    TIMECODE : "float",
    OBJECT : "object",
    FRACTION : "float",
    SELECT : "text",
    LIST : "text",
    COLOR : "integer",
}


async def prepare():
    spinner = halo.Halo(text="Connecting to Elastic search", spinner="dots")
    spinner.start()

    properties = {}
    for key in meta_types.keys():
        meta_type = meta_types[key]
        properties[key] = {
            "type": CLASS_TO_ES_TYPE[meta_type["class"]]
        }

    spinner.text = "Deleting old index"
    await elastic.es.indices.delete(index="assets", ignore=[404])

    spinner.text = "Installing new index"
    await elastic.es.indices.create(
        index="assets", 
        body={
            "settings" : es_settings,
            "mapping" : {
                "properties" : properties
            }
        }
    )

    spinner.succeed(text="Elastic search configured")







spinner = halo.Halo(text="Loading data...", spinner="dots")
spinner.start()
data = json.load(open("/data/import/assets.json"))
spinner.succeed("Data loaded")
for meta in data:
    safe_get_asset(**meta)


sys.exit(0)


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

        for key in ["aired", "audio_tracks"]:
            if key in meta:
                del(meta[key])

        await es.index(index='assets', id=aid,body=meta)
        await redis.set("asset" + str(aid), json.dumps(meta))
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


#asyncio.run(prepare())
#asyncio.run(store())
#asyncio.run(validate_records())


loop = asyncio.get_event_loop()
try:
    elastic.connect()
    loop.run_until_complete(prepare())
    loop.run_until_complete(elastic.close())
finally:
    loop.close()