import matplotlib.pyplot as plt

# Data for stem-and-leaf
stems = [1, 2, 3]
leaves = [
    [9],              # Leaves for stem 1
    [0, 2, 6, 7, 8],  # Leaves for stem 2
    [1, 2, 3, 4]      # Leaves for stem 3
]

# Prepare data for plotting
stem_labels = [f"{stem} | {' '.join(map(str, leaf))}" for stem, leaf in zip(stems, leaves)]
leaf_counts = [len(leaf) for leaf in leaves]  # Number of leaves per stem

# Plot
plt.figure(figsize=(8, 5))
plt.barh(stem_labels, leaf_counts, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Number of Leaves', fontsize=12)
plt.ylabel('Stem | Leaves', fontsize=12)
plt.title('Stem-and-Leaf Plot Visualization', fontsize=14)

# Add values on the bars
for i, count in enumerate(leaf_counts):
    plt.text(count + 0.1, i, str(count), va='center', fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()
