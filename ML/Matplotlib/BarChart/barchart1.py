import numpy as np
from matplotlib import pyplot as plt

python = (12, 2, 34, 65)
java = (20, 12, 42, 59)
networking = (42, 32, 38, 25)
machine_learning = (24, 29, 84, 95)

people = ["Bob", "Anna", "John", "Mark"]

index = np.arange(4)

plt.bar(index, python, width=0.2, label="python")
plt.bar(index + 0.2, java, width=0.2, label="java")
plt.bar(index + 0.4, networking, width=0.2, label="networking")
plt.bar(index + 0.6, machine_learning, width=0.2, label="ML")

plt.title("IT Skills")
plt.xlabel("Person")
plt.ylabel("Skill Level")

plt.xticks(index + 0.2, people)
plt.ylim(0, 100)
plt.legend(loc="upper left")
plt.show()
plt.close()
