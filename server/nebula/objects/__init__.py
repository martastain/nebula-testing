from ..common import *
from ..metadata import meta_types


class Asset():
    def __init__(self, **kwargs) -> None:
        self.meta = kwargs

    def __getitem__(self, key):
        return self.meta(key, meta_types[key].default)

    def __repr__(self):
        return "<Asset>"

    def show(self, key, **kwargs):
        return meta_types[key].show(self, key, **kwargs)



def safe_get_asset(**kwargs):
    for key in kwargs:
        if not key in meta_types:
        #   print ("Ignoring unknown key", key)
            continue

        value = meta_types[key].validate(kwargs[key])
        if value != kwargs[key]:
            print("FIXED {}: {}({}) -> {}({})".format(key, kwargs[key], type(kwargs[key]), value, type(value)))
        

