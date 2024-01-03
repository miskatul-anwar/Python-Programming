#!python
import os
import csv
file= open("phonebook.csv","a")

nm = input("Name: ")
name = nm.capitalize()

number = input("Phone: ")
writer = csv.writer(file)
writer.writerow([name,number])
file.close()

os.system("open phonebook.csv")
