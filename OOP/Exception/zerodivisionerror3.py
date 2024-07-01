class Function:
    def __init__(self):
        pass

    def div(self, x, y):
        try:
            res = x / y
        except ZeroDivisionError:
            print("Division by Zero")
        else:
            return res
        finally:
            print("Done")


def main():
    foo = Function()
    print(foo.div(1, 2))


if __name__ == "__main__":
    main()
