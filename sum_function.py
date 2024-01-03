#! python
#this is a summation printing function

def sum(x,y):
    print("x + y = ",x+y)
def sub(x,y):
    print("x - y = ",x-y)
def mul(x,y):
    print("x * y = ",x*y)
def div(x,y):
    if(y>0 or y<0):
        print("x / y = ",x/y)
    else:
        print("Error! Division result can't be shown.")

x=int(input("x = ")) ;y=int(input("y = "))

sum(x,y)
sub(x,y)
mul(x,y)
div(x,y)