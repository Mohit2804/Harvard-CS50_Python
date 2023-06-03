from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid Date")

    print(birth_date(year, month, day))

def birth_date(year, month, day):
    try:
        date_of_birth = date(int(year), int(month), int(day))
        today_date = date.today()
        diff = today_date - date_of_birth
        minutes = diff.days * 24 * 60
        word = p.number_to_words(minutes, andword="")
        return word.capitalize() + " minutes"
    except ValueError:
        return "Invalid Date"

if __name__ == "__main__":
    main()
