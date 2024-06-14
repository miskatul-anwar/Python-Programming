import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Create a figure and axis
fig, ax = plt.subplots()

# Draw a circle
circle = Circle((0.5, 0.5), 0.4, color="b", fill=False)

# Add the circle to the axis
ax.add_patch(circle)

# Set equal aspect ratio
ax.set_aspect("equal", adjustable="box")

# Set limits for the axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add a title
ax.set_title("Circle")

# Show the plot
plt.show()
