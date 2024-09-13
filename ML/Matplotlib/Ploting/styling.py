from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

# style.use("fivethirtyeight")
"""
style.use("ggplot")
style.use("Solarize_Light2")
style.use("dark_background")
style.use("ggplot")
style.use("grayscale")
"""

# Grid
plt.grid(True)

# Title
plt.title("Sine Function")

# Suptitle
plt.suptitle("f(x)=sin(x)")

# x label
plt.xlabel("x")

# y label
plt.ylabel("y")

x = np.arange(0,30,0.2)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,'r',label="sine")
plt.plot(x,y2,'g',label="cosine")
plt.legend(loc='upper left')
plt.show()
