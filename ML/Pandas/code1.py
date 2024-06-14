import pandas as pd
import pyfiglet

list = []


def input_system(nm):
    list.append(nm)
    data = pd.DataFrame(list)
    print(data)


def main():
    name_of_the_system = "Products Management System"
    formatted_name = pyfiglet.figlet_format(name_of_the_system)
    print(formatted_name)
    while True:
        name = input("Enter name of the product: ")
        nm = name.capitalize()
        if nm == "Stop" or nm == "Quit":
            cond = input("Do you want to quit?y/n")
            cn = cond.capitalize()
            if cn == "Y":
                break
            else:
                continue
        input_system(nm)


main()
