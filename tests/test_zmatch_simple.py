from zmatch import check

input_data = {
    "user_id": "12345",  # String
    "age": 30,  # Integer
    "height": 5.9,  # Float
    "is_active": True,  # Boolean
    "email": "john.doe@example.com",  # String
    "address": {
        "street": "123 Elm St",  # String
        "city": "Metropolis",  # String
        "zipcode": 12345  # Integer
    },
    "preferences": {
        "notifications": True,  # Boolean
        "newsletter_subscription": False,  # Boolean
        "theme": "dark"  # String
    },
    "salary": 85000.50,  # Float
    "activity_log": [
        {"date": "2024-11-01", "action": "login", "status": "success"},  # Dict
        {"date": "2024-11-05", "action": "purchase", "status": "success", "item": "Laptop"}  # Dict
    ]
}


# Test for integer matching
def test_zmatch_int():
    predicate = {"age": 30}
    assert check(input_data, predicate) is True

def test_zmatch_int_not_match():
    predicate = {"age": 35}
    assert check(input_data, predicate) is False

# Test for string matching
def test_zmatch_str():
    predicate = {"user_id": "12345"}
    assert check(input_data, predicate) is True

def test_zmatch_str_not_match():
    predicate = {"user_id": "67890"}
    assert check(input_data, predicate) is False

# Test for float matching
def test_zmatch_float():
    predicate = {"height": 5.9}
    assert check(input_data, predicate) is True

def test_zmatch_float_not_match():
    predicate = {"height": 6.0}
    assert check(input_data, predicate) is False

# Test for boolean matching
def test_zmatch_bool():
    predicate = {"is_active": True}
    assert check(input_data, predicate) is True

def test_zmatch_bool_not_match():
    predicate = {"is_active": False}
    assert check(input_data, predicate) is False
