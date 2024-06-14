def rhombus(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(" ", end=" ")
        for j in range(n):
            print("* ", end="")
        print()


def main():
    n = int(input("Enter number of rows: "))
    rhombus(n)


main()
