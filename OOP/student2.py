import pyfiglet


def print_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)


class student:
    text = "Loading..."
    print_ascii_art(text)

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


name = input("enter the name of the student: ")
age = int(input("enter the age of the student: "))
marks = int(input("enter the marks of the student: "))
s = student(name, age, marks)
print(s.name)
print(s.age)
print(s.marks)
