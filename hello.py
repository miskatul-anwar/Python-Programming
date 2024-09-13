def hello(name: str) -> None:
    print(f"Hello, {name} !")


def main() -> None:
    name = str(input("Enter your name: "))
    hello(name)


if __name__ == "__main__":
    main()
