import matplotlib.pyplot as plt
import numpy as np

# Define heart shape
t = np.linspace(0, 2 * np.pi, 100)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Plot the filled heart shape
plt.fill(x, y, "red")

# Customize plot appearance
plt.title(
    "You have such a genuine warmth that brightens everyone's day.\n Your kindness is like a ray of sunshine,\n Always spreading positivity wherever you go.",
    fontdict={
        "fontsize": "12",
        "fontweight": "bold",
        "fontstyle": "italic",
        "fontname": "Times New Roman",
    },
    loc="center",
)
plt.axis("off")  # Turn off axis
plt.gca().set_aspect("equal", adjustable="box")  # Equal aspect ratio
plt.show()
