__all__ = ["Asset", "asset_factory"]

from ..common import *
from ..metadata import meta_types



class BaseObject():
    def __init__(self, **kwargs) -> None:
        self.meta = kwargs

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




def asset_factory(metadata):
    asset = Asset()
    for key in metadata:
        if not key in meta_types:
            continue

        value = meta_types[key].validate(metadata[key])
        if value != metadata[key]:
            print("FIXED {}: {}({}) -> {}({})".format(key, metadata[key], type(metadata[key]), value, type(value)))
    
        asset.meta[key] = value
    return asset
