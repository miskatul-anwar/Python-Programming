num=int(input("Enter the number of rows you want:"))
sum=1
for row in range(1,num+1):
    for col in range(1,sum+1):
        print("* ", end=" ")
    sum=sum+2
    print("\n")
