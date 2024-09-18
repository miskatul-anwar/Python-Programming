import sys

n = int(input("Enter number of data to be stored: "))
data = []
for i in range(n):
    if i == 0:
        print("Enter data on " + str(i + 1) + "st index: ")
    elif i == 1:
        print("Enter data on " + str(i + 1) + "nd index: ")
    elif i == 2:
        print("Enter data on " + str(i + 1) + "rd index: ")
    else:
        print("Enter data on " + str(i + 1) + "th index: ")
    dat = int(input())
    data.append(dat)
print(f"{data}")
avarage = sum(data) / len(data)
print("The Avarage: " + str(avarage))
sys.exit(1)

# ==> simple a program to print the avarage of given inputs
# --> this is using an array of n elements to get the data
