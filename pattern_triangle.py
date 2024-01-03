#this is a program to print a triangle 
print("Enter (row,column) ")

#input integer type variable
row=int(input(  "row="))
col=int(input(  "col="))

#initialization
#main body
for x in range(1,row+1):
    for y in range(1,x+1):
        print("*",end=' ')
    print("\n")   
