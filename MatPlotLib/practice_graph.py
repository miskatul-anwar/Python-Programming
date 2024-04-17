import matplotlib.pyplot as plt
import numpy as np

x, y = [1, 2, 3, 4, 5], [5, 25, 65, 24, 5]
x_ticks, y_ticks = np.arange(0, 0.5, 6), np.arange(0, 0.5, 65)
plt.plot(x, y)
plt.show()
