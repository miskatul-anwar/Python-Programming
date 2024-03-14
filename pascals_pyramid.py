def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def coefficient(m, n):
    return factorial(m) / (factorial(n) * factorial(m - n))


def main():
    n = int(input("Enter a number: "))
    for i in range(n + 1):
        for j in range(n - i + 1):
            print(end=" ")
        for j in range(i + 1):
            g = int(coefficient(i, j))
            print(g, end=" ")
        print()
    return 0


main()
