
def setup_function(function):
    global application_id
    print(f"\nRunning Setup: {function.__name__}")
    application_id = "123"

def teardown_function(function):
    print(f"\nRunning Teardown: {function.__name__}")

def test_all_functions():
    assert application_id == "123"