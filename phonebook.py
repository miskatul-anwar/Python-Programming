#! python
import sys
people = {
    "Miskat": "01864010558",
    "Jasmine": "01816053986",
    "Shafi": "01713473538"
}
while True:
 nm = input("Name: ")
 name = nm.capitalize() 
 if name in people:
    print(f"Number: {people[name]}")
    sys.exit("Thanks!")
 else:
    sys.exit("Sorry! Not available.")



#==> simple use of sys.exit() function (^_^)
