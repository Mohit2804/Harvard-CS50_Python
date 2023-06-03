from seasons import birth_date

def main():
    test1()
    test2()

def test1():
    assert birth_date(1996, 4, 28) == "Fourteen million, two hundred forty-eight thousand, eight hundred minutes"
    assert birth_date(2023, 5, 1) == "Forty-four thousand, six hundred forty minutes"

def test2():
    assert birth_date(28, 4, 1996) == "Invalid Date"

if __name__ == "__main__":
    main()
