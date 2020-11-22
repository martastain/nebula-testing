__all__ = ["meta_types"]

from ..common import *
from .validators import class_validators
from .defaults import *

default_type = {
    "name" : "",
    "class" : 0,
    "default" : "" 
}

class MetaType():
    def __init__(self, **kwargs):
        self.data = {
            "name" : "",
            "aliases" : {},
            **kwargs
        }

    def default(self):
        return self.data["default"]

    def alias(self, language="en"):
        for alias in [
            self.data["aliases"].get(language),
            self.data["aliases"].get("en"),
            self.data["name"]
        ]:
            if alias is not None:
                return alias

    def __getitem__(self, key):
        return self.data[key] 

    def show(self, value, object=False, **kwargs):
        return str(value)

    def validate(self, value, object=False):
        return class_validators[self["class"]](object, self["name"], value)




class MetaTypes():
    def __iter__(self):
        return self.keys().__iter__()

    def keys(self) -> list:
        return list(config["meta_types"].keys())

    def __getitem__(self, key) -> MetaType:
        return MetaType(**config["meta_types"].get(key, {"name" : key, **default_type} ))

meta_types = MetaTypes()