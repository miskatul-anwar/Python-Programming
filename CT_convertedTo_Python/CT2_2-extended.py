#importing library
import math as mt

#showing the point definition
print("Enter (x,y):")

#entering the (x,y) point
x=input("  x=")
y=input("  y=")

#type conversion
x=int(x)
y=int(y)

#condition part
z=int(mt.pow((5-x),2)+mt.pow((7-y),2))
if z>0 and z <=7:
    print("Inside")
else:
    print("Outside")

