import csv
file = open("phonebook2.csv","a")
nm = input("Name: ")
name = nm.capitalize()
number = input("Phone: ")
em = input("E-mail: ")
email = em.lower()

write = csv.Dictwriter(file, fieldnames=["Name", "Number", "E-mail"])
write.writerow({"Name": name, "Number": number, "E-mail": email})
file.close()
