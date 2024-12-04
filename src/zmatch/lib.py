import typing
import re

from .helpers import (
    _is_str,
    _is_str_list,
    _is_int,
    _is_int_list,
    _is_float,
    _is_float_list,
    _is_bool,
    _is_bool_list,
    _is_dict,
    _is_dict_list,
    _is_list
)

def check_str(
    data: str,
    expected_match: str | typing.Dict[str, typing.Any],
) -> bool:
    if not _is_str(data):
        return False
    
    if _is_str(expected_match):
        return data == expected_match
    
    if not _is_dict(expected_match):
        return False

    if len(expected_match) != 1:
        return False
    first_key = list(expected_match.keys())[0]
    if first_key not in [
        '__is', 
        '__not', 
        '__in', 
        '__not_in', 
        '__matches', 
        '__not_matches'
    ]:
        print("We are here")
        return False
    
    if first_key == '__is' and _is_str(expected_match[first_key]):
        return data == expected_match[first_key]
    if first_key == '__not' and _is_str(expected_match[first_key]):
        return data != expected_match[first_key]
    if first_key == '__in' and _is_str_list(expected_match[first_key]):
        return data in expected_match[first_key]
    if first_key == '__not_in' and _is_str_list(expected_match[first_key]):
        return data not in expected_match[first_key]
    if first_key == '__matches' and _is_str(expected_match[first_key]):
        return re.match(expected_match[first_key], data) is not None
    if first_key == '__not_matches' and _is_str(expected_match[first_key]):
        return re.match(expected_match[first_key], data) is None

    return False

def check_int(
    data: int,
    expected_match: int | typing.Dict[str, typing.Any],
) -> bool:
    if not _is_int(data):
        return False
    
    if _is_int(expected_match):
        return data == expected_match
    
    if not _is_dict(expected_match):
        return False
    if len(expected_match) != 1:
        return False
    
    first_key = list(expected_match.keys())[0]
    if first_key not in [
        '__is', 
        '__not', 
        '__in', 
        '__not_in',
        '__gt',
        '__lt',
        '__gte',
        '__lte'
    ]:
        return False

    if first_key == '__is' and _is_int(expected_match[first_key]):
        return data == expected_match[first_key]
    if first_key == '__not' and _is_int(expected_match[first_key]):
        return data != expected_match[first_key]
    if first_key == '__in' and _is_int_list(expected_match[first_key]):
        return data in expected_match[first_key]
    if first_key == '__not_in' and _is_int_list(expected_match[first_key]):
        return data not in expected_match[first_key]
    if first_key == '__gt' and _is_int(expected_match[first_key]):
        return data > expected_match[first_key]
    if first_key == '__lt' and _is_int(expected_match[first_key]):
        return data < expected_match[first_key]
    if first_key == '__gte' and _is_int(expected_match[first_key]):
        return data >= expected_match[first_key]
    if first_key == '__lte' and _is_int(expected_match[first_key]):
        return data <= expected_match[first_key]
    
    return False

def check_float(
    data: float,
    expected_match: float | typing.Dict[str, typing.Any],
) -> bool:
    if not _is_float(data):
        return False
    
    if _is_float(expected_match):
        return data == expected_match
    
    if not _is_dict(expected_match):
        return False
    if len(expected_match) != 1:
        return False
    
    first_key = list(expected_match.keys())[0]
    if first_key not in [
        '__is', 
        '__not', 
        '__in', 
        '__not_in',
        '__gt',
        '__lt',
        '__gte',
        '__lte'
    ]:
        return False

    if first_key == '__is' and _is_float(expected_match[first_key]):
        return data == expected_match[first_key]
    if first_key == '__not' and _is_float(expected_match[first_key]):
        return data != expected_match[first_key]
    if first_key == '__in' and _is_float_list(expected_match[first_key]):
        return data in expected_match[first_key]
    if first_key == '__not_in' and _is_float_list(expected_match[first_key]):
        return data not in expected_match[first_key]
    if first_key == '__gt' and _is_float(expected_match[first_key]):
        return data > expected_match[first_key]
    if first_key == '__lt' and _is_float(expected_match[first_key]):
        return data < expected_match[first_key]
    if first_key == '__gte' and _is_float(expected_match[first_key]):
        return data >= expected_match[first_key]
    if first_key == '__lte' and _is_float(expected_match[first_key]):
        return data <= expected_match[first_key]
    
    return False

def check_bool(
    data: bool,
    expected_match: bool | typing.Dict[str, typing.Any],
) -> bool:
    if not _is_bool(data):
        return False
    
    if _is_bool(expected_match):
        return data == expected_match
    
    if not _is_dict(expected_match):
        return False
    if len(expected_match) != 1:
        return False
    
    first_key = list(expected_match.keys())[0]
    if first_key not in [
        '__is', 
        '__not'
    ]:
        return False

    if first_key == '__is' and _is_bool(expected_match[first_key]):
        return data == expected_match[first_key]
    if first_key == '__not' and _is_bool(expected_match[first_key]):
        return data != expected_match[first_key]
    
    return False

def check_dict(
    data: typing.Dict[typing.Any, typing.Any],
    expected_match: typing.Dict[typing.Any, typing.Any],
):
    if not _is_dict(data):
        return False
    
    if not _is_dict(expected_match):
        return False
    
    if len(expected_match) > len(data):
        return False
    
    for key, match_value in expected_match.items():
        if key not in data:
            return False
        
        data_value = data[key]
        if data_value is None and match_value is None:
            continue

        if _is_str(data_value):
            sub_is_match = check_str(data_value, match_value)
            if not sub_is_match:
                return False

        elif _is_int(data_value):
            sub_is_match = check_int(data_value, match_value)
            if not sub_is_match:
                return False

        elif _is_float(data_value):
            sub_is_match = check_float(data_value, match_value)
            if not sub_is_match:
                return False

        elif _is_bool(data_value):
            sub_is_match = check_bool(data_value, match_value)
            if not sub_is_match:
                return False
        
        elif _is_dict(data_value):
            sub_is_match = check_dict(data_value, match_value)
            if not sub_is_match:
                return False
        
        elif _is_list(data_value):
            sub_is_match = check_list(data_value, match_value)
            if not sub_is_match:
                return False

        elif data_value != match_value:
            return False
    return True

def check_list(
    data: typing.List[typing.Any],
    expected_match: typing.List[typing.Any] | typing.Dict[str, typing.Any],
):
    if not _is_list(data):
        return False
    
    if _is_list(expected_match):
        return data == expected_match
    
    if not _is_dict(expected_match):
        return False
    
    if _is_dict_list(data):
        return any({
            check_dict(item, expected_match) for item in data
        })

    # We are expecting expected_match to be a dict which has only one condition key
    if len(expected_match) != 1:
        return False
    
    first_key = list(expected_match.keys())[0]

    if _is_int_list(data):
        if first_key not in [
            '__contains',
            '__not_contains'
        ]:
            return False
        if first_key == '__contains' and _is_int(expected_match[first_key]):
            return any([item == expected_match[first_key] for item in data])

        
        if first_key == '__not_contains' and _is_int(expected_match[first_key]):
            return any([item != expected_match[first_key] for item in data])
        
        return False
    
    if _is_float_list(data):
        if first_key not in [
            '__contains',
            '__not_contains'
        ]:
            return False
        if first_key == '__contains' and _is_float(expected_match[first_key]):
            return any([item == expected_match[first_key] for item in data])
        
        if first_key == '__not_contains' and _is_float(expected_match[first_key]):
            return any([item != expected_match[first_key] for item in data])
        
        return False
    
    if _is_str_list(data):
        if first_key not in [
            '__contains',
            '__not_contains'
        ]:
            return False
        if first_key == '__contains' and _is_str(expected_match[first_key]):
            return any([item == expected_match[first_key] for item in data])
        
        if first_key == '__not_contains' and _is_str(expected_match[first_key]):
            return any([item != expected_match[first_key] for item in data])
        
        return False
    
    if _is_bool_list(data):
        if first_key not in [
            '__contains',
            '__not_contains'
        ]:
            return False
        if first_key == '__contains' and _is_bool(expected_match[first_key]):
            return any([item == expected_match[first_key] for item in data])
        
        if first_key == '__not_contains' and _is_bool(expected_match[first_key]):
            return any([item != expected_match[first_key] for item in data])
        
        return False

def check(
    data: typing.Dict[typing.Any, typing.Any],
    expected_match: typing.Dict[typing.Any, typing.Any],
):
    if data is None:
        raise ValueError("data cannot be None")

    if expected_match is None:
        raise ValueError("expected_match cannot be None")

    # type checking
    if not isinstance(data, dict):
        raise ValueError("data must be a dictionary")

    if not isinstance(expected_match, dict):
        raise ValueError("expected_match must be a dictionary")

    return check_dict(
        data=data,
        expected_match=expected_match
    )