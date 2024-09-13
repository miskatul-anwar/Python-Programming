def main():
    while True:
        name = str(input("Enter string: "))
        match name:
            case "miskat":
                print("foo")
            case "Hello":
                print("neib")
            case _:
                print("Who? ")


if __name__ == "__main__":
    main()
