import numpy as np
import matplotlib.pyplot as plt


# Define the function
def f(x):
    return 4 * x**2 + 5


# Generate x values
x = np.linspace(0, 10, 100)  # Generating 100 points between 0 and 10

# Generate y values using the function
y = f(x)

# Plot the function
plt.figure(figsize=(8, 6))  # Adjusting figure size for better visualization
plt.plot(
    x, y, label="f(x) = 4x^2 + 5", color="b", linewidth=2
)  # Customize color and line width
plt.title("Graph of f(x) = 4x^2 + 5")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle="--", alpha=0.7)  # Customize grid appearance
plt.legend()  # Show legend
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
