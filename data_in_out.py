import os
import csv
file = open("Data-Sheet.csv", "a")
nm = input("Name: ")
name = nm.capitalize()
id = input("Id: ")

wr = csv.writer(file)
wr.writerow([name, id])
os.system("open Data-Sheet.csv")
