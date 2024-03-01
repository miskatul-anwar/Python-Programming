# this is program to check conditions
s = input("Do you agree?")
if s.lower() in ["y", "yes"]:
    print("Agreed")
elif s.lower() in ["n", "no"]:
    print("Disagreed")
else:
    print("Enter valid data")
