import matplotlib.pyplot as plt
import numpy as np

myplot = plt.axes(projection="3d")

x_data = np.arange(0, 20, 0.1)
y_data = np.arange(0, 20, 0.1)
X, Y = np.meshgrid(x_data, y_data)
Z = X * Y

myplot.plot_surface(X, Y, Z)
plt.show()
