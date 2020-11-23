from nxtools import *

from ..constants.meta_classes import *

def string_formater(object, key, value, mode, **kwargs):
    return value

def text_formater(object, key, value, mode, **kwargs):
    return value

def integer_formater(object, key, value, mode, **kwargs):
    return str(value)

def numeric_formater(object, key, value, mode, **kwargs):
    return str(value)

def boolean_formater(object, key, value, mode, **kwargs):
    return str(value)

def datetime_formater(object, key, value, mode, **kwargs):
    return format_time(value)

def timecode_formater(object, key, value, mode, **kwargs):
    return s2tc(value)

def object_formater(object, key, value, mode, **kwargs):
    return value

def fraction_formater(object, key, value, mode, **kwargs):
    return value

def select_formater(object, key, value, mode, **kwargs):
    return value

def list_formater(object, key, value, mode, **kwargs):
    return value

def color_formater(object, key, value, mode, **kwargs):
    return value
    
    


class_formaters = {
    STRING : string_formater,
    TEXT : text_formater,
    INTEGER : integer_formater,
    NUMERIC : numeric_formater,
    BOOLEAN : boolean_formater,
    DATETIME : datetime_formater,
    TIMECODE : timecode_formater,
    OBJECT : object_formater,
    FRACTION  : fraction_formater,
    SELECT : select_formater,
    LIST : list_formater,
    COLOR : color_formater,
}