from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes()

# Plot for f(x) = sin(x)
# let's consider, y = f(x) = sin(x)

x_data = np.arange(0, 20, 0.1)
y_data = np.sin(x_data)

ax.set_title("f(x) = sin(x)", font="Maple Mono", color="red")
ax.set_xlabel("sin(x)")
ax.set_ylabel("sin(x)")
ax.plot(x_data, y_data)
plt.show()
