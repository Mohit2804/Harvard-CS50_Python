bank = input("Greetings? ").strip().lower()
word = bank[0:5]
letter = bank[0]

if word == "hello":
    print("$0")

elif letter == "h":
    print("$20")
else:
    print("$100")
