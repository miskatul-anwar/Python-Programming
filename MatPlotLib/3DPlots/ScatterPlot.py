import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")

x_data = np.arange(0, 100, 10)
y_data = np.arange(0, 100, 10)
z_data = np.arange(0, 100, 10)

ax.scatter(x_data, y_data, z_data, color="red", marker="v", alpha=0.9)

plt.show()
