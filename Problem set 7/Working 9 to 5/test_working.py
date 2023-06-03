from working import convert
import pytest

def main():
    test1()
    test2()
    test3()

def test1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test2():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test3():
    with pytest.raises(ValueError):
        convert("7:65 AM to 12:65 PM")
    with pytest.raises(ValueError):
        convert("9AM to 9PM")
    with pytest.raises(ValueError):
        convert("08:00 to 17:00")
    with pytest.raises(ValueError):
        convert("8 AM - 8 PM")
    with pytest.raises(ValueError):
        convert("08:00 AM - 18:00")
