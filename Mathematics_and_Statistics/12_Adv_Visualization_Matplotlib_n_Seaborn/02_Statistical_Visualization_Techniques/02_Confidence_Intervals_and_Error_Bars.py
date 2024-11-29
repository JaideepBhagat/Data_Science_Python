import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("sakshisatre/tips-dataset")
tips = pd.read_csv(os.path.join(path, "tip.csv"))
# Add error bars using ci:
sns.lineplot(x='size', y='total_bill', data=tips, ci='sd')
# Add Title
plt.title('Line Plot with Error Bars')
# Add Labels
plt.xlabel('Size')
plt.ylabel('Total Bill')
# Show the plot
plt.show()