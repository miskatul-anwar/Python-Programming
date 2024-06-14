import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")

x_data = np.arange(0, 10, 0.1)
y_data = np.arange(0, 10, 0.1)
z_data = x_data * y_data

# ax.scatter(x_data, y_data, z_data, alpha=0.5, color="black")
ax.plot(x_data, y_data, z_data)

plt.show()
