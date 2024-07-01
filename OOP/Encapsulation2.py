class SimpleClass:
    def __init__(self, name) -> None:
        print("An Instance of Simple Class created")
        self.name = name

    def dev(self, x: int, y: int) -> float:
        try:
            return x / y
        except ZeroDivisionError:
            print("zero div error")
        finally:
            print("Handled !")


def main():
    foo = SimpleClass("Answer")
    print(f"{foo.name} is : {foo.dev(5,2)}\n")


if __name__ == "__main__":
    main()
