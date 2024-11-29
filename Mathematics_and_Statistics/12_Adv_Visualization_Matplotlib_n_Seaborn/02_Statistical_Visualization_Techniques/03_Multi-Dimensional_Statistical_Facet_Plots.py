import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("sakshisatre/tips-dataset")
tips = pd.read_csv(os.path.join(path, "tip.csv"))
# Multi-Dimensional Statistics using FacetGrid
sns.relplot(x='total_bill', y='tip', hue='day', col='time', size='sex', data=tips)
# Show the plot
plt.show()