#!/usr/bin/env python3

import http
import sanic

from api import API

SERVER_NAME = "NEBULA 6"
DEFAULT_HEADERS = {
        "Server" : SERVER_NAME,
        "Access-Control-Allow-Origin" : "*",
        "Access-Control-Allow-Methods" : "*"
    }

app = sanic.Sanic(SERVER_NAME)
api = API()

def response(status_code=200, message=None, **kwargs):
    """Create a raw data API response

    Args:
        response (int): Response status code to be included in the resulting JSON object
        message (str): Textual description of the call status. Defaults to a HTTP
            response message defined by the "response" argument
        **kwargs: Additional data to be included in the resulting JSON object

    Returns:
        sanic.response.json

    """
    if message is None:
        message = http.client.responses[status_code]
    return sanic.response.json({
                "response" : status_code,
                "message" : message,
                **kwargs
             },
             headers={
                    **DEFAULT_HEADERS,
                 }
         )

def raw_response(mime="application/octet-stream", data=b""):
    """Create a raw data API response

    Args:
        mime (str): MIME type of the response. Defaults to application/octet-stresm
        data (bytes): Response body

    Returns:
        sanic.response.raw

    """
    return sanic.response.raw(
            data,
            headers={
                    **DEFAULT_HEADERS,
                    "Content-Type" : mime,
                }
        )


@app.route("/api/<method:string>", methods=["GET", "POST"])
async def api_request(request, method):

    kwargs = request.args
    for key in kwargs:
        if len(kwargs[key]) == 1:
            kwargs[key] = kwargs[key][0]

    method = getattr(api, method, None)
    if method is None:
        return response(400, "No such method")

    result = await method(**kwargs)
    return response(**result)


app.static("/", "frontend/index.html")

#@app.route("/", methods=["GET"])
#async def index_request(request):
#    with f

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200, debug=True)
