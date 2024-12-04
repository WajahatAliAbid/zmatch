def _is_str(value):
    return isinstance(value, str)

def _is_str_list(value):
    return isinstance(value, list) and all([isinstance(item, str) for item in value])


def _is_int(value):
    return isinstance(value, int) and not isinstance(value, bool)

def _is_int_list(value):
    return isinstance(value, list) and all([isinstance(item, int) and not isinstance(item, bool) for item in value])

def _is_float(value):
    return isinstance(value, float) and not isinstance(value, bool)

def _is_float_list(value):
    return isinstance(value, list) and all([isinstance(item, float) and not isinstance(item, bool) for item in value])

def _is_bool(value):
    return isinstance(value, bool)

def _is_bool_list(value):
    return isinstance(value, list) and all([isinstance(item, bool) for item in value])

def _is_dict(value):
    return isinstance(value, dict)

def _is_dict_list(value):
    return isinstance(value, list) and all([isinstance(item, dict) for item in value])

def _is_list(value):
    return isinstance(value, list)