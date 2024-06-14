list = []


def loop(n):
    if n == 1 or n == 0:
        return 1
    return loop(n - 1) + loop(n - 2)


def fibonacci(n):
    if n == 0:
        return 0
    else:
        print(loop(n - 1), end=" ")
    return fibonacci(n - 1)


def main():
    n = int(input("Enter the number of terms:"))
    fibonacci(n)


main()
