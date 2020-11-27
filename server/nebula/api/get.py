from ..common import *
from ..cache import *

from .responses import *

async def api_get(**kwargs):
    try:
        id_object = int(kwargs["id"])
    except KeyError:
        return response(400, "You must provide id of the object")
    except ValueError:
        return response(400, "Object id must be an integer")

    meta = await cache.get("asset", id_object)

    return response(200, data=meta)


