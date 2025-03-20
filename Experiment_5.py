#Skewed data
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import boxcox

# Generate skewed data (right-skewed)
data = np.random.exponential(scale=2, size=1000)

# Apply Box-Cox transformation to reduce skewness
data_transformed, _ = boxcox(data + 1)  # Adding 1 to avoid zero values

# Plot original and transformed data
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(data, kde=True, ax=axes[0])
axes[0].set_title("Original Skewed Data")

sns.histplot(data_transformed, kde=True, ax=axes[1])
axes[1].set_title("Transformed Data (Reduced Skewness)")

plt.show()
