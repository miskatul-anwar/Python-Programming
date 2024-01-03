import sys
while True: 
    print("Type 'exit' to leave current session: ")
    response=input()
    if response == 'exit': sys.exit(1)
    print("You typed"+response+".")

#-> this is a simple program ==> for exiting (^_^) 
#now, pass the below command:
#==>echo $? -> to check the exitcode
#>= 0 and == 1 shows that it's working
