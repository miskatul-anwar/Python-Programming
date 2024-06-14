import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.legend()
ax.set_title("Simple plot")
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()
