print("\t\bEnter your name:")
usr_name = input()
print("Welcome..!"+' '+usr_name+', '+"Enter your age:")
usr_age = input()
if int(usr_age) < 18: print("Gen alpha")
if 18<= int(usr_age) < 26: print("Gen Z")
if 26<= int(usr_age) < 35: print("Millennials")
if 35<= int(usr_age) < 45: print("Gen X")
if 45<= int(usr_age) < 60: print("Baby Boomers")
if 60<= int(usr_age) < 80: print("Silent")
else : print("No relevant naming for your Generation.")
print("\tThank You.")
