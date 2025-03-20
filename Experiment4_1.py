# ECDF
import numpy as np
import matplotlib.pyplot as plt

# Generate normally distributed data
data_1 = np.random.normal(0, 1, 1000)

# Sort the data
data_sorted = np.sort(data_1)

# Compute ECDF values
y_values = np.arange(1, len(data_sorted) + 1) / len(data_sorted)

# Plot ECDF using a step plot for clarity
plt.figure(figsize=(8, 6))
plt.step(data_sorted, y_values, where='post', color='b', linewidth=2, label="ECDF")  # Step plot
plt.scatter(data_sorted, y_values, color='red', s=10, alpha=0.6)  # Add markers for individual points
plt.xlabel('Data Values')
plt.ylabel('ECDF')
plt.title('Empirical Cumulative Distribution Function (ECDF)')
plt.legend()
plt.grid(True)
plt.show()
