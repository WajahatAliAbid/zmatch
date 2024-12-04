import pytest
import json
import os.path
import zmatch

def load_test_data(file_name: str):
    _path = os.path.join(os.path.dirname(__file__), "data", f"{file_name}.json")
    with open(_path, "r") as fs:
        data = json.load(fs)
    return [
        (item['input'], item['test'], item['output']) for item in data
    ]

@pytest.mark.parametrize("input, test, assertion", load_test_data("strings"))
def test_strings(input, test, assertion):
    assert zmatch.check_str(input, test) == assertion

@pytest.mark.parametrize("input, test, assertion", load_test_data("strings_bad"))
def test_strings_bad(input, test, assertion):
    assert zmatch.check_str(input, test) == assertion

@pytest.mark.parametrize("input, test, assertion", load_test_data("ints"))
def test_ints(input, test, assertion):
    assert zmatch.check_int(input, test) == assertion


@pytest.mark.parametrize("input, test, assertion", load_test_data("floats"))
def test_floats(input, test, assertion):
    assert zmatch.check_float(input, test) == assertion
    