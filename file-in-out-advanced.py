import os
import csv

with open("phonebook.csv", "a") as file:
    nm = input("Name: ")
    name = nm.capitalize()
    num = input("Phone: ")
    wr = csv.writer(file)
    wr.writerow([name, num])
os.system("open phonebook.csv")
