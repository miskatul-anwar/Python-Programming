class student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome", self.name)


s = student("Ram", 90)
print(s.college_name)
print(s.name)
print(s.marks)
