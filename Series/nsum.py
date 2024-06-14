def nsum(n):
    idx = 0
    for i in range(n + 1):
        for j in range(i):
            idx = idx + 1
            print(idx, end=" ")
        print("|", end=" ")


def main():
    nsum(5)


if __name__ == "__main__":
    main()
