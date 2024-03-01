while True:
    try:
        n = int(input("Height=>"))
        if n > 0:
            return n
    except ValueError:
        print("Invalid input")
