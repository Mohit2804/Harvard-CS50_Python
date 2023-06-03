from bank import value

def main():
    test_zero()
    test_20()
    test_100()

def test_zero():
    assert value('Hello mo') == 0
    assert value('Hello') == 0
    assert value('HeLlo mo') == 0

def test_20():
    assert value('Hi') == 20
    assert value('hey') == 20
    assert value('hii') == 20

def test_100():
    assert value('Mohit') == 100
    assert value('Good morning') == 100
    assert value("What's up?") == 100

if __name__ == "__main__":
    main()
