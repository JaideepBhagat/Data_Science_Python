import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("sakshisatre/tips-dataset")
tips = pd.read_csv(os.path.join(path, "tip.csv"))
# Plot the bar plot and box plot
fig, ax = plt.subplots(1, 2, figsize=(10, 5))  # Create a figure with two subplots
sns.barplot(x='day', y='total_bill', data=tips, ax=ax[0])  # Plot the bar plot in the first subplot
sns.boxplot(x='day', y='total_bill', data=tips, ax=ax[1])  # Plot the box plot in the second subplot
plt.tight_layout()
plt.show()