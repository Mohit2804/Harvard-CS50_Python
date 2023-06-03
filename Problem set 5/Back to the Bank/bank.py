def main():
    greeting = input("Greetings? ")
    bank = value(greeting)
    print(f"${bank}")

def value(greeting):
    greeting = greeting.strip().lower()
    word = greeting[0:5]
    letter = greeting[0]

    if word == "hello":
        return 0

    elif letter == "h":
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()
