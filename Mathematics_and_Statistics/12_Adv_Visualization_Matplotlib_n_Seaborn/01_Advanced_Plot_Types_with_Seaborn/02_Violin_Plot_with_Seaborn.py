import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("sakshisatre/tips-dataset")

tips = pd.read_csv(os.path.join(path, "tip.csv"))
# Plot the violin plot
sns.violinplot(x='day', y='total_bill', data=tips)
# Add Title
plt.title('Violin Plot Example')
# Add Labels
plt.xlabel('Day')
plt.ylabel('Total Bill')
# Show the plot
plt.show()