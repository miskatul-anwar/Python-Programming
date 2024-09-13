import matplotlib.pyplot as plt
from mpl_toolkit import mplot3d
import numpy as np
ax = plt.axes(projection="3d")
z = np.linspace(0,30,100)
x = np.sin(z)
y = np.cos(z)

ax.plot3d(x,y,z)
plt.show()