__all__ = ["api"]

from ..common import config

from .responses import response
from .browse import api_browse
from .get import api_get

class API():
    async def browse(self, **kwargs) -> response:
        """ Browse assets

        Args:
          v (int): id_view. 
            If set to -1, no view will be used (no default filter or keys)
            If set to 0, the first available view will be used.
          q (str): full-text search query
          p (int): page number (starting with 1) 
          l (int): number of records presented in one page
          s (string): key used for sorting
          d (bool): sort in a descending order (default is an ascending)
        """
        return await api_browse(**kwargs)

    async def views(self, **kwargs) -> response:
        """ List views available to the user"""

        data = {
            "global" : [],
            "user" : []
        }
        for id_view in config["views"].keys():
            data["global"].append({
                "id": id_view,
                "title" : config["views"][id_view]["title"]
            })

        return response(200, data=data)

    async def get(self, **kwargs) -> response:
        """ Get a single object"""
        return await api_get(**kwargs)




api = API()
