__all__ = ["response", "raw_response", "SERVER_NAME"]

import sanic
import http

SERVER_NAME = "NEBULA 6"
DEFAULT_HEADERS = {
        "Server" : SERVER_NAME,
        "Access-Control-Allow-Origin" : "*",
        "Access-Control-Allow-Methods" : "*"
    }

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
