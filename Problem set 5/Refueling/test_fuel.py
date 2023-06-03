from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_gauge():
    assert gauge(16) == "16%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


if __name__ == "__main__":
    main()
