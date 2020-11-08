#!/usr/bin/env python3
import sys
import asyncio
import pprint

from api import search
from api import API

api = API()

async def test(query):
    r = await api.suggest(query)
    await search.close()
    pprint.pprint(r)

asyncio.run(test(
    " ".join(sys.argv[1:])
    ))

