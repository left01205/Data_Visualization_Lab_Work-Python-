# Load the new dataset
import pandas as pd

# Load the dataset
file_path = "Path To dataset"
df = pd.read_csv(file_path)

# Display basic information about the dataset
df.info(), df.head(3)


import matplotlib.pyplot as plt
import seaborn as sns

# Select a subset of data for better visualization (top 10 locations with most records)
top_locations = df["Location"].value_counts().head(10).index
df_subset = df[df["Location"].isin(top_locations)]

# Compute aggregate values
avg_max_temp = df_subset.groupby("Location")["MaxTemp"].mean().sort_values()
total_rainfall = df_subset.groupby("Location")["Rainfall"].sum().sort_values()
avg_humidity = df_subset.groupby("Location")[["Humidity9am", "Humidity3pm"]].mean()

# Set up figure for multiple bar plots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Bar plot for average max temperature per location
avg_max_temp.plot(kind="bar", ax=axes[0], color="royalblue", edgecolor="black")
axes[0].set_title("Average Max Temperature per Location")
axes[0].set_ylabel("Temperature (°C)")

# Bar plot for total rainfall per location
total_rainfall.plot(kind="bar", ax=axes[1], color="darkgreen", edgecolor="black")
axes[1].set_title("Total Rainfall per Location")
axes[1].set_ylabel("Rainfall (mm)")

# Bar plot for humidity at 9 AM and 3 PM per location
avg_humidity.plot(kind="bar", ax=axes[2], color=["purple", "orange"], edgecolor="black")
axes[2].set_title("Average Humidity Levels at 9 AM and 3 PM")
axes[2].set_ylabel("Humidity (%)")

plt.tight_layout()
plt.show()
