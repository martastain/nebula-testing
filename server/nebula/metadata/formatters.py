__all__ = ["class_formatters"]

from ..common import *

def string_formatter(object, key, value, mode, **kwargs):
    return value

def text_formatter(object, key, value, mode, **kwargs):
    if mode == "listing":
        return value.split("\n")[0][:200]
    return value

def integer_formatter(object, key, value, mode, **kwargs):
    return str(value)

def numeric_formatter(object, key, value, mode, **kwargs):
    return str(value)

def boolean_formatter(object, key, value, mode, **kwargs):
    return str(value)

def datetime_formatter(object, key, value, mode, **kwargs):
    return format_time(value)

def timecode_formatter(object, key, value, mode, **kwargs):
    if object and object["video/fps_f"]:
        return s2tc(value, object["video/fps_f"])
    else:
        return s2time(value)

def object_formatter(object, key, value, mode, **kwargs):
    return str(value)

def fraction_formatter(object, key, value, mode, **kwargs):
    return value

def select_formatter(object, key, value, mode, **kwargs):
    return value

def list_formatter(object, key, value, mode, **kwargs):
    return value

def color_formatter(object, key, value, mode, **kwargs):
    return value
    
    


class_formatters = {
    STRING : string_formatter,
    TEXT : text_formatter,
    INTEGER : integer_formatter,
    NUMERIC : numeric_formatter,
    BOOLEAN : boolean_formatter,
    DATETIME : datetime_formatter,
    TIMECODE : timecode_formatter,
    OBJECT : object_formatter,
    FRACTION  : fraction_formatter,
    SELECT : select_formatter,
    LIST : list_formatter,
    COLOR : color_formatter,
}