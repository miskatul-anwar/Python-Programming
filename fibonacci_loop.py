def fibonacci(n):
    fib1, fib2 = 1, 0
    for it in range(n + 1):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
    return fib2


def main():
    n = int(input("Enter a number: "))
    print("The ", n, "th fibonacci number is: ", fibonacci(n), end="\n")


if __name__ == "__main__":
    main()
