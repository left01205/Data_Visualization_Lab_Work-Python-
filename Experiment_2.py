
# Load the new dataset
import pandas as pd

# Load the dataset
file_path = "Path to dataset"
df = pd.read_csv(file_path)

# Display basic information about the dataset
df.info(), df.head(3)


import matplotlib.pyplot as plt
import seaborn as sns

# Compute the correlation matrix for numerical columns
corr_matrix = df.corr(numeric_only=True)

# Define different color scales
color_maps = ["coolwarm", "viridis", "plasma", "magma", "cividis"]

# Set up the figure size
fig, axes = plt.subplots(1, len(color_maps), figsize=(20, 5))

# Generate heatmaps with different color scales
for ax, cmap in zip(axes, color_maps):
    sns.heatmap(corr_matrix, cmap=cmap, annot=False, ax=ax)
    ax.set_title(f"Heatmap - {cmap}")

plt.tight_layout()
plt.show()
