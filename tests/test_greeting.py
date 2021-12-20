from greeting import my_name, your_name

def test_my_name():
    assert "My name is: bob" == my_name("bob")

def test_your_name():
    assert "your name is Lisa" == your_name()