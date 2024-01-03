#a simple program to print a rectangle
print("Enter (height,width): ")

#input section
x=int(input(  "height="));y=int(input(  "width="))

#main body
for i in range(1,x+1):
    for j in range(1,y+1):
        print("* ", end=' ')
    print("\n")
