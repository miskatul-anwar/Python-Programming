import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
categories = ["A", "B", "C", "D"]
values = [10, 23, 17, 5]
ax = plt.bar(categories, values)
plt.xlabel("marks", font="Maple Mono")
plt.ylabel("marks", font="Maple Mono")
plt.title("CSE 116 Marks", font="Maple Mono")
plt.legend("CSE116", loc="lower left")
# ax.bar(langs, students)
plt.show()
