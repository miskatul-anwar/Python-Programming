# --> ? for a given function f(x) = 4 x * x  draw the graphical representation

# importing all the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    return 4 * x**2


# Labeling
plt.title("f(x) = 4*x^2")
plt.xlabel("x")
plt.ylabel("y")

# values for x, y
x = np.linspace(0, 5, 100)
y = f(x)

plt.plot(x, y)
plt.grid(True)
plt.show()
