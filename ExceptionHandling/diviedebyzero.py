def spam(nom, denom):
    try:
        return nom / denom
    except ZeroDivisionError:
        print("Invalid argument")
    else:
        print("HI")


def main():
    spam(5, 0)


if __name__ == "__main__":
    main()
