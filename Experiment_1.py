import pandas as pd

df = pd.read_csv("Path to dataset")

import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")

# Create scatter plot
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    x=df["sqft_living"],
    y=df["price"],
    hue=df["bedrooms"],
    palette="viridis",
    alpha=0.6
)

# Labels and title
plt.xlabel("Living Area (sqft)")
plt.ylabel("Price ($)")
plt.title("House Prices vs. Living Area (Colored by Bedrooms)")
plt.legend(title="Bedrooms", bbox_to_anchor=(1, 1))
plt.show()
