#!/usr/bin/env python3
import sys
import json
import halo
import asyncio
import aioredis
import elasticsearch

print("\n")

spinner = halo.Halo(text="Loading data...", spinner="dots")
spinner.start()
data = json.load(open(sys.argv[1]))
spinner.succeed("Data loaded")


async def get_redis():
    return await aioredis.create_redis_pool('redis://redis')

es = elasticsearch.AsyncElasticsearch(["elastic"])

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


asyncio.run(store())
asyncio.run(validate_records())

