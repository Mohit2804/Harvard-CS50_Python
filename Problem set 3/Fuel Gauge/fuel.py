while True:
    fuel = input("Fraction: ")
    try:
        X, Y = fuel.split("/")
        n_X = int(X)
        n_Y = int(Y)
        fraction = n_X / n_Y
        if fraction <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass

percent = round(fraction * 100)

if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")
