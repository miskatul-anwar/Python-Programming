import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(0, 2 * np.pi, 200)
x = np.sin(y)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
