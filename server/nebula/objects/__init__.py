__all__ = ["Asset", "asset_factory"]

from ..common import *
from ..metadata import meta_types


class BaseObject():
    def __init__(self, id=False, meta=False) -> None:
        if id:
            logging.error("Loading by ID is not implemented")
        elif meta:
            self.meta = meta
        else:
            self.meta = {}

    def __iter__(self):
        return self.meta.keys().__iter__()

    def __getitem__(self, key):
        return self.meta.get(key, meta_types[key].get_default())

    def __repr__(self):
        return "<Asset>"

    def show(self, key, mode=False, **kwargs):
        return meta_types[key].show(
                value=self[key], 
                object=self, 
                mode=mode, 
                **kwargs
            )


class Asset(BaseObject):
    pass




def asset_factory(meta:dict) -> Asset:
    """Returns an asset based on the dict of metadata, similar to calling `asset = Asset(meta=meta)`  
    Additionally, asset_factory performs type checking including fixing the most common problems with
    incorrectly formated metadata. It is threrefore a little bit slower, but it is good to use this
    function when importing assets from an external source.

    Args:
        meta (dict): Dictionary object with metadata

    Returns:
        Asset: Asset object instance, or None, if there is an unrecoverable error during processing

    """
    asset = Asset()
    for key in meta:
        if not key in meta_types:
            continue
        value = meta_types[key].validate(meta[key])
        if value != meta[key]:
            logging.warning("FIXED {}: {}({}) -> {}({})".format(key, meta[key], type(meta[key]), value, type(value)))
        asset.meta[key] = value
    return asset

