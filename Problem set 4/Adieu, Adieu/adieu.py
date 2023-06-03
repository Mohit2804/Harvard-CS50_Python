import inflect
p = inflect.engine()

names = []

while True:
    try:
        a = input("Name: ")
        names.append(a)
    except:
        print()
        break

output = p.join(names)
print("Adieu, adieu, to " + output)
