## <u>Matplotlib</u>
***
*Let's Start With Some Basic **Plotting** Examples: 
```python
from numpy import *
from pylab import *

x = arange(-10, 10, 0.5)
y = x**2
plot(x, y, "r.")
show()

```
### Histogram
```python
import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
categories = ["A", "B", "C", "D"]
values = [10, 23, 17, 5]
ax = plt.bar(categories, values)
plt.xlabel("marks", font="Maple Mono")
plt.ylabel("marks", font="Maple Mono")
plt.title("CSE 116 Marks", font="Maple Mono")
plt.legend("CSE116", loc="lower left")
# ax.bar(langs, students)
plt.show()
```

### Graphs
#### f(x) = sin(x)
```python
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

```

### 3D
#### Sphere
```python
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

```
#### Scatter Plot
##### 01
```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")

x_data = np.arange(0, 10, 0.1)
y_data = np.arange(0, 10, 0.1)
z_data = x_data * y_data

# ax.scatter(x_data, y_data, z_data, alpha=0.5, color="black")
ax.plot(x_data, y_data, z_data)

plt.show()

```
#### 02
```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")

x_data = np.arange(0, 100, 10)
y_data = np.arange(0, 100, 10)
z_data = np.arange(0, 100, 10)

ax.scatter(x_data, y_data, z_data, color="red", marker="v", alpha=0.9)

plt.show()

```
#### Surface Plot
```python
import matplotlib.pyplot as plt
import numpy as np

myplot = plt.axes(projection="3d")

x_data = np.arange(0, 20, 0.1)
y_data = np.arange(0, 20, 0.1)
X, Y = np.meshgrid(x_data, y_data)
Z = X * Y

myplot.plot_surface(X, Y, Z)
plt.show()

```