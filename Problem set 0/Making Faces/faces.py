def main():
    print(convert())

def convert():
    faces = input("Typr here: ")
    faces = faces.replace(":)", "🙂")
    faces = faces.replace(":(", "🙁")
    return faces
if __name__ == "__main__":
    main()
