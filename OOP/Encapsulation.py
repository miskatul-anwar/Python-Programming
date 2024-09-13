class SimpleClass:
    def __init__(self) -> None:
        print("An Instance of Simple Class created")

    def dev(self, x: int, y: int) -> float:
        try:
            return x / y
        except ZeroDivisionErro:
            print("zero div error")
        finally:
            print("Handled !")


def main():
    foo = SimpleClass()
    print(foo.dev(5, 0))


if __name__ == "__main__":
    main()
