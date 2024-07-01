class Funcions:
    def __init__(self):
        pass

    def divide(self, x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("Error: Division by zero")
            return None
        else:
            return result


def main():
    # Create an instance of the Funcions class
    funcions_instance = Funcions()

    # Example usage with try-except-else using pure OOP principles
    result = funcions_instance.divide(10, 2)
    if result is not None:
        print(
            f"Result: {result}"
        )  # This will print the result if no exception was raised


if __name__ == "__main__":
    main()
