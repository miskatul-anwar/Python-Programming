from matplotlib import pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x,y,c='r',marker='*',s=100)
plt.show()
