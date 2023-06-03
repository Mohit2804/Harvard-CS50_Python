import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except:
        pass

random_num = random.randint(1, n)

while True:
    try:
        g = int(input("Guess: "))
        if g > 0:
            if g < random_num:
                print("Too small!")
            elif g > random_num:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass
