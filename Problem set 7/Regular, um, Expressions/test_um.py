from um import count

def main():
    test1()
    test2()
    test3()

def test1():
    assert count("um") == 1

def test2():
    assert count("Um, thanks for the album.") == 1
    assert count("Hello, world") == 0

def test3():
    assert count("Um, thanks, um...") == 2

if __name__ == "__main__":
    main()
