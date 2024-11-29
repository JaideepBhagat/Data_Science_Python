import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("sakshisatre/tips-dataset")

tips = pd.read_csv(os.path.join(path, "tip.csv"))

# Plot the joint and marginal distributions
sns.jointplot(x='total_bill', y='tip', data=tips)
# Add Title
plt.title('Joint and Marginal Distribution Example')
# Add Labels
plt.xlabel('Total Bill')
plt.ylabel('Tip')
# Show the plot
plt.show()