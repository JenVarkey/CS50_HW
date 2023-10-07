from plates import is_valid

def test_is_valid():
    assert is_valid("GHEJ26") == True
    assert is_valid("GH222H") == False
    assert is_valid("GH0226") == False
    assert is_valid("GHJK22222") == False
    assert is_valid("GHJ*22") == False
    assert is_valid("GHJKDL") == True
    assert is_valid("33") == False
