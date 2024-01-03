#! python
people ={
    "Carter": "01864010558",
    "Matt": "01816053986"
}
name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")
