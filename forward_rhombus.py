def rhombus(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(" ", end="")
        for j in range(n + 1):
            print("* ", end="")
        print()


def main():
    rows = int(input("Enter the number of rows: "))
    rhombus(rows)


main()
