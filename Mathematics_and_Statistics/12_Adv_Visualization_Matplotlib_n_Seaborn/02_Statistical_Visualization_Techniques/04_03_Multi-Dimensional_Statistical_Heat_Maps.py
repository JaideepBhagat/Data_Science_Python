import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("sakshisatre/tips-dataset")
tips = pd.read_csv(os.path.join(path, "tip.csv"))
# Multi-Dimensional Statistics with Heat Maps
sns.heatmap(tips.pivot_table(index='day', columns='time', values='total_bill', aggfunc='mean'))
# Show the plot
plt.show()