scores = []
for i in range(5):
    score = int(input("Enter "+str(i+1)+"st value:"))
    scores += [score]
    print(f"{scores}")
avarage = sum(scores) / len(scores)
print()
print("Avarage: "+str(avarage))

