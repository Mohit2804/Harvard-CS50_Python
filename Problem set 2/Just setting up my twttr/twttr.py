word = input("Input: ")
print("Output: ", end="")


for l in word:
    if l.lower() not in ["a", "e", "i", "o", "u"]:
        print(l, end="")

print()
