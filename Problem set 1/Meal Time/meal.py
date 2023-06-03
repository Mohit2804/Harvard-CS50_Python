def main():
    meal = input("What time it is? ")
    time = convert(meal)

    if 7 <= time <= 8:
        print("Breakfast Time")
    elif 12 <= time <= 13:
        print("Lunch Time")
    elif 18 <= time <= 19:
        print("Dinner Time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    if len(minutes) > 2:
        minutes, end = minutes.split(" ")
        if end == "a.m.":
            hours = hours
        elif end == "p.m.":
            hours = hours + 12

    n_minutes = float(minutes) / 60
    time = float(hours) + n_minutes
    return time

if __name__ == "__main__":
    main()
