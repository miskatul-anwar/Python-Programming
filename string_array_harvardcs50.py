#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#
# This is a simple practice of string_arrays #
#==#==#==#==#==#==#==#==#==#==#==#==#==#==#==#
import sys
names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

name = input("Name to look for: ")

if name in names:
    print("Found!")
    sys.exit(0)
print("Not found!")
sys.exit(1)
