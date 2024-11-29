import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
sales = pd.read_csv(os.path.join(path, "train.csv"))
# Plot the heatmap
sns.heatmap(sales.pivot_table(index='Region', columns='Category', values='Sales', aggfunc='sum'))
# Show the plot
plt.show()