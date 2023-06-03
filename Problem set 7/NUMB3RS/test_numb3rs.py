from numb3rs import validate

def main():
    test_num_format()
    test_num_range()

def test_num_format():
    assert validate(r'1.3.2.4') == True
    assert validate(r'1.3.4') == False
    assert validate(r'1.10.5.15') == True
    assert validate(r'1.3') == False

def test_num_range():
    assert validate(r'0.255.0.255') == True
    assert validate(r'0.1000.0.255') == False
    assert validate(r'0.255.400.255') == False
    assert validate(r'0.600.0.255') == False

if __name__ == "__main__":
    main()
