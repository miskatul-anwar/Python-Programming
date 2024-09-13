import numpy as np

x = np.linspace(0,1000,100) # -> inclusive
y = np.arange(0,1000,100) # -> exclusive
z = np.array([
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    ],dtype=float)

print(x)
print(y)
print(z)

print(f"This is the size of x: {x.size}")
print(f"This is the size of y: {y.size}")
