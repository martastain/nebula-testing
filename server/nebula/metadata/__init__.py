__all__ = ["meta_types"]

from ..common import *
from .validators import class_validators
from .formaters import class_formaters
from .defaults import *

default_type = {
    "name" : "",
    "class" : 0,
    "default" : "",
    "alias" : {}
}

CLASS_DEFAULTS = {
    STRING : "",
    TEXT : "",
    INTEGER : 0,
    NUMERIC : 0,
    BOOLEAN : False,
    DATETIME : 0,
    TIMECODE : 0,
    OBJECT : {},
    FRACTION  : "1/1",
    SELECT : "",
    LIST : [],
    COLOR : 0,
}

class MetaType():
    def __init__(self, **kwargs):
        self.data = {
            **default_type,
            **kwargs
        }

    def __getitem__(self, key):
        return self.data[key] 

    def get_default(self):
        return self.data.get("default", CLASS_DEFAULTS[self["class"]])

    def get_alias(self, language="en"):
        for alias in [
            self.data["alias"].get(language),
            self.data["alias"].get("en"),
            self.data["name"]
        ]:
            if alias is not None:
                return alias

    def show(self, value, object=False, mode=False, **kwargs):
        return class_formaters[self["class"]](
            object, 
            self["name"], 
            value,
            mode, 
            **kwargs
        )

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