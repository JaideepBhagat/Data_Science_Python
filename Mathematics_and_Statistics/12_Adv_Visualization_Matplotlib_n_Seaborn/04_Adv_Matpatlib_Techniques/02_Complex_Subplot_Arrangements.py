import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
import os
import pandas as pd
# Download sales data
path = kagglehub.dataset_download("sakshisatre/tips-dataset")
tips = pd.read_csv(os.path.join(path, "tip.csv"))
print(path)
# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
# Plot the sales data in the first subplot
sns.boxplot(x='sex', y='tip', data=tips, ax=axs[0, 0], palette='light:lightblue', hue='smoker')
axs[0, 0].set_title('Tip by Gender')
# Plot the bar chart in the second subplot
sns.violinplot(x='smoker', y='total_bill', data=tips, ax=axs[0, 1], palette='light:lightgreen', hue='sex')
axs[0, 1].set_title('Bill by Smokers')
# Plot the scatter plot in the third subplot
sns.barplot(x='day', y='total_bill', data=tips, ci='sd', ax=axs[1, 0], palette= 'pastel')
axs[1, 0].set_title('Sales by Region')
# Plot the histogram in the fourth subplot
sns.kdeplot(tips['total_bill'], ax=axs[1, 1], fill=True, color='g')
axs[1, 1].set_title('Sales Distribution')
# Adjust spacing between subplots
plt.tight_layout()
# Show the plot
plt.show()