from pylab import *
from numpy import *

# To begin with, we create a figure instance which provides an empty canvas.
# fig = figure()

# Now add axes to figure. The add_axes() method requires a list object of 4 elements
# corresponding to left, bottom, width and height of the figure. Each number must be
# between 0 and 1:
# ax = fig.add_axes([0, 0, 1, 1])

# Set labels for x and y axis as well as title:
ax = axes()
ax.set_title("sine wave")
ax.set_xlabel("angle")
ax.set_ylabel("sine")
x = arange(0, pi * 2, 0.05)
y = sin(x)
ax.legend(lebels=("tv", "smarphone"), loc="lower right")
# Invoke the plot() method of the axes object.
ax.plot(x, y)
show()
