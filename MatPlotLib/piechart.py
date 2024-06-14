import matplotlib.pyplot as plt

# Data to plot
labels = ["Apple", "Banana", "Orange", "Grapes"]
sizes = [25, 30, 20, 25]  # Sizes or proportions of each slice
colors = ["red", "yellow", "orange", "green"]  # Colors for each slice
explode = (0.1, 0, 0, 0)  # Explode 1st slice (i.e. 'Apple')

# Plot
plt.figure(figsize=(6, 6))  # Adjust figure size

plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=140,
)

plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Fruit Distribution")

plt.show()
