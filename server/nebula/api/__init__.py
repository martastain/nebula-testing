__all__ = ["api"]

from ..common import config

from .responses import response
from .browse import api_browse

class API():
    async def browse(self, **kwargs) -> response:
        """ Browse assets

        Args:
          v (int): id_view. 
            If set to -1, no view will be used (no default filter or keys)
            If set to 0, the first available view will be used.
          q (str): full-text search query
          l (int):
          o (int):
        """
        return await api_browse(**kwargs)

    async def views(self, **kwargs) -> response:
      """ List views available to the user
      """

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




api = API()
