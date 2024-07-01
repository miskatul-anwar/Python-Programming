import os


def spam(n):
    os.system("firefox -new-tab https://youtube.com &")
    spam(n - 1)


def main():
    spam(10)


if __name__ == "__main__":
    main()
