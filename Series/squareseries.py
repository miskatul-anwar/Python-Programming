# 1^1 + 2^2 + 3^3 + . . . + n^n
import numpy as np


def sq(n):
    x = 0
    for i in range(n + 1):
        x = x + i * i
    return x


def main():
    n = int(input("Enter a number: "))
    print(sq(n))
    return 0


if __name__ == "__main__":
    main()
