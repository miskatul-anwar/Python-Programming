scores = []
for i in range(5):
    score = int(input("Enter "+str(i+1)+"st element:"))
    scores.append(score)
avarage = sum(scores) / len(scores)
print(f"The avarage of:{scores}")
print("Avarage Score is: "+str(avarage))
