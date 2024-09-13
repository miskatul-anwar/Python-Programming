with open("hi.txt", "w") as f:
    f.write("hellow")

with open("hi.txt") as f:
    print(f.read())
