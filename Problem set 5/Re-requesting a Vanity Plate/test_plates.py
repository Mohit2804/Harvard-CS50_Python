from plates import is_valid

def main():
    test_is_valid1()
    test_is_valid2()
    test_is_valid3()
    test_is_valid4()

def test_is_valid1():
    assert is_valid("m") == False
    assert is_valid("Good, morning") == False
    assert is_valid("CS50") == True

def test_is_valid2():
    assert is_valid("12") == False
    assert is_valid("cs") == True

def test_is_valid3():
    assert is_valid("cs.,10") == False
    assert is_valid("cs10") == True
    assert is_valid("cs50p") == False

def test_is_valid4():
    assert is_valid("cs05") == False
    assert is_valid("cs50") == True

if __name__ == "__main__":
    main()
