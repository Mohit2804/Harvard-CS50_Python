calc = input("Expression: ")
x, y, z = calc.split(" ")
nx = float(x)
nz = float(z)

if y == "+":
    print(nx + nz)

elif y == "-":
    print(nx - nz)

elif y == "*":
    print(nx * nz)

elif y == "/":
    print(nx / nz)

else:
    print("Invalid Expression")
