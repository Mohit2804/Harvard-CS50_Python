def main():
    text = input("Input: ")
    text_omit_vowels = shorten(text)
    print("Output: " + text_omit_vowels)

def shorten(word):
    word_omit_vowels = ""
    for l in word:
        if l.lower() not in ["a", "e", "i", "o", "u"]:
            word_omit_vowels += l

    return word_omit_vowels


if __name__ == "__main__":
    main()
