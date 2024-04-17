import matplotlib.pyplot as plt

x, y = [1, 2, 3], [4, 5, 6]
plt.title(
    "A 2D graph",
    fontdict={
        "fontname": "Cambria",
    },
)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xticks([1, 2, 3, 4])
plt.yticks([1, 2, 3, 4])
plt.plot(x, y)
plt.show()
