from bank import value

def test_value():
    assert value("Hey") == 20
    assert value("Hello") == 0
    assert value("Good Morning") == 100