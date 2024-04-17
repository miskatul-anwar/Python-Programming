import matplotlib.pyplot as plt

x, y = [1, 2, 3, 4, 5], [1, 4, 9, 16, 25]
x_ticks, y_ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.title("A Basic Graph")
plt.plot(x, y)
plt.show()
