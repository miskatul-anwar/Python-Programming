import numpy as np
from matplotlib import pyplot as plt

mu, sigma = 172, 8
x = mu + sigma * np.random.randn(1000)

plt.hist(x,100,facecolor='blue',density=True)
plt.xlabel("Heights")
plt.ylabel("Percentage of Students")
plt.grid(True)
plt.show()
