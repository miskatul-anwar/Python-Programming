def main():
    try:
        print(5 / 0)
    except ZeroDivisionError:
        print("hi")
    else:
        print("foo")
