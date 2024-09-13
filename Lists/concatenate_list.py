catNames = []
while True:
    name = str(
        input(f"Enter the name of the cat {len(catNames)+1} or enter nothing to stop:")
    )
    if name == "":
        break
    catNames += [name]

print(catNames)
