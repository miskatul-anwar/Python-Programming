#This is ANC CT02-02
print("Enter (x,y): ")
x=input("x=")
y=input("y=")
x=int(x)
y=int(y)

z=(5-x)**2 + (7-y)**2
z=int(z)

if z>=0 and z<=7:
    print("Inside")
else:
    print("Outside")

