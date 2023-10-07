from twttr import shorten


def test_assert():
    assert shorten("Meap9") == "Mp9"
    assert shorten("HEllo") == "Hll"
    assert shorten("Goodbye!") == "Gdby!"
    assert shorten("Apple Slices") == "ppl Slcs"
