#!/usr/bin/env python3

import sanic

from nebula.api import API
from nebula.api.responses import response, SERVER_NAME

app = sanic.Sanic(SERVER_NAME)
api = API()

@app.route("/api/<method:string>", methods=["GET", "POST"])
async def api_request(request, method):
    """ API entry point 
    """

    kwargs = request.args
    #TODO:
    # - parse POST (form encoded and json body)
    # - sessions
    # - auth
    # - error handling

    for key in kwargs:
        if len(kwargs[key]) == 1:
            kwargs[key] = kwargs[key][0]

    method = getattr(api, method, None)
    if method is None:
        return response(400, "No such method")

    result = await method(**kwargs)
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200, debug=True)
