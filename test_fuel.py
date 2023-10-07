from fuel import convert, gauge
import pytest
def test_fuel():
    print(convert("1/100"))
    assert convert("1/100") == 0
    assert gauge(convert("1/100")) == "E"
    assert gauge(convert("23/45")) == "51%"
    assert gauge(convert("2/3")) == "67%"
    assert gauge(convert("99/100")) == "F"
    with pytest.raises(ZeroDivisionError):
       gauge(convert("10/0"))
    with pytest.raises(ValueError):
       gauge(convert(7/4))