#this is anc ct 2 problem 1
i=0
temperature=input("Enter a temperature: ")
if int(temperature) > 50 and int(temperature) < 90:
    i=i+1
elif int(temperature) > 30 and int(temperature) < 45:
    i=i+1
elif int(temperature) > 0 and int(temperature) < 10:
    i=i+1
elif int(temperature) > 6 and int(temperature) < 9:
    i=i+1

if int(i)==3:
    print("Extreme")
elif int(i)>3:
    print("Ultra")
elif int(i)<3:
    print("Superb")
else:
    print("Not valid")
