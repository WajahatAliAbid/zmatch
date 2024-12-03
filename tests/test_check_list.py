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
    "numbers": [
        1,2,3,4
    ],
    "salary": 85000.50,  # Float
    "activity_log": [
        {"date": "2024-11-01", "action": "login", "status": "success"},  # Dict
        {"date": "2024-11-05", "action": "purchase", "status": "success", "item": "Laptop"}  # Dict
    ]
}

def test_check_list():
    assert check(
        input_data, expected_match={
            "numbers": [1,2,3,4]
        }
    )

def test_match_single_item():
    assert check(
        input_data, expected_match={
            "numbers": {
                "__contains": 1
            }
        }
    )