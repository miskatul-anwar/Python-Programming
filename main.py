from prompt_toolkit import prompt


def print_name(name: str, times: int) -> None:
    for _ in range(times):
        print("my name is " + name)
    return


def main() -> None:
    times: int = int(prompt("Enter how many times: "))
    name: str = prompt("Enter your name: ")
    print_name(name, times)


if __name__ == "__main__":
    main()
