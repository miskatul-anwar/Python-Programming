from typing_extensions import overload


class Overload:
    def __init__(self) -> None:
        pass

    @overload
    def greetings(self) -> None: ...

    @overload
    def greetings(self, name: str) -> None: ...

    def greetings(self, name: str = None) -> None:
        if name is None:
            print("Hello")
        else:
            print(f"Hello, {name}")


def main():
    foo = Overload()
    foo.greetings("Miskat")


if __name__ == "__main__":
    main()
