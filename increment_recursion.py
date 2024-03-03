#! python
def loop(target, current=1):
    if current <= target:
        print(current)
        loop(target, current + 1)


def main():
    n = int(input("Enter a number: "))
    loop(n, 1)


main()
