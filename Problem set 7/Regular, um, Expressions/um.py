import re

def main():
    print(count(input("Text: ")))

def count(s):
    count_word = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(count_word)

if __name__ == "__main__":
    main()
