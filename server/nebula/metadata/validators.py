import json

from ..constants.meta_classes import *


def text_validator(object, key, value):
    if type(value) in [int, float, bool]:
        value = str(value)
    else:
        assert type(value) == str, "String is expected"
    return value

def string_validator(object, key, value):
    value = text_validator(object, key, value)
    assert "\n" not in value, "Only one line is allowed"
    return value

def integer_validator(object, key, value):
    if type(value) == str and value.isnumeric():
        value = int(value) 
    elif type(value) == float:
        value = int(value)
    else:
        assert type(value) == int, "Integer value is expected"
    return value

def numeric_validator(object, key, value):
    assert type(value) in [int, float], "Numeric value is expected"
    return value

def boolean_validator(object, key, value):
    if not value:
        return False
    if value in ["false", "0", "False"]:
        return False
    return True

def datetime_validator(object, key, value):
    value = numeric_validator(object, key, value)
    return value

def timecode_validator(object, key, value):
    value = numeric_validator(object, key, value)
    return value

def object_validator(object, key, value):
    try:
        r = json.dumps(value)
    except:
        raise AssertionError("Object is not serializable")
    return value

def fraction_validator(object, key, value):
    assert type(value) == str
    try:
        n,d = [int(k) for k in value.split("/")]
    except:
        raise AssertionError("Unknown fraction format")
    return value

def select_validator(object, key, value):
    assert type(value) == str, "String is expected"
    return value

def list_validator(object, key, value):
    assert type(value) == list, "List is expected"
    assert all([type(k) == str for k in value]), "All list values must be of string type"
    return value

def color_validator(object, key, value):
    value = integer_validator(object, key, value)
    return value
    
    


class_validators = {
    STRING : string_validator,
    TEXT : text_validator,
    INTEGER : integer_validator,
    NUMERIC : numeric_validator,
    BOOLEAN : boolean_validator,
    DATETIME : datetime_validator,
    TIMECODE : timecode_validator,
    OBJECT : object_validator,
    FRACTION  : fraction_validator,
    SELECT : select_validator,
    LIST : list_validator,
    COLOR : color_validator,
}