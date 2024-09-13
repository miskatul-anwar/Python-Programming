from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")

# Create a sphere using numpy
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(v), np.sin(u))
y = np.outer(np.sin(v), np.sin(u))
z = np.outer(np.ones(np.size(u)), np.cos(u))
ax.plot_surface(x, y, z, color="r", rstride=4, cstride=4)

plt.show()
