import typing
from .helper import matches_str, matches_number, matches_bool


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
    
    # This means expected_match can be a subset of data
    if len(expected_match) > len(data):
        return False    
    
    for key in expected_match:
        match_value = expected_match[key]
        if key not in data:
            return False
        
        data_value = data[key]
        if data_value is None and match_value is None:
            continue

        if isinstance(data_value, str):
            sub_is_match = matches_str(data_value, match_value)
            if not sub_is_match:
                return False
            
        elif isinstance(data_value, (int, float)):
            sub_is_match = matches_number(data_value, match_value)
            if not sub_is_match:
                return False
        
        elif isinstance(data_value, bool):
            sub_is_match = matches_bool(data_value, match_value)
            if not sub_is_match:
                return False
        
        elif isinstance(data_value, dict):
            if not isinstance(match_value, dict):
                return False
            sub_is_match = check(data_value, match_value)
            if not sub_is_match:
                return False
        elif isinstance(data_value, list):
            if isinstance(match_value, list):
                return data_value == match_value   
        elif data_value != match_value:
            return False

    return True