import matplotlib.pyplot as plt

# Data
prices = [3.88, 3.90, 3.93, 3.94, 3.96, 3.98, 3.99]
relative_frequencies = [0.231, 0.154, 0.154, 0.154, 0.154, 0.077, 0.077]

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(prices, relative_frequencies, marker='o', linestyle='-', color='b', label='Relative Frequency')

# Add labels and title
plt.title('Relative Frequency Line Graph', fontsize=14)
plt.xlabel('Price ($)', fontsize=12)
plt.ylabel('Relative Frequency', fontsize=12)

# Grid and legend
plt.grid(alpha=0.5, linestyle='--')
plt.legend()

# Display the graph
plt.tight_layout()
plt.show()

