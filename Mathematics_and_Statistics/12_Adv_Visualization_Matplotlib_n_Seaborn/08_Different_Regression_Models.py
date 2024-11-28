import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("sakshisatre/tips-dataset")

tips = pd.read_csv(os.path.join(path, "tip.csv"))

# Multiple Linear Regression Plot
sns.lmplot(x='total_bill',  # Total bill as input variable (x-axis)
           y='tip',  # Tip as output variable (y-axis)
           hue='sex',  # Color by gender
           data=tips,  # Data source
           palette='Set1',  # Color palette
           robust=True)  # Robust regression
# Add Title
plt.title('Multiple Linear Regression Plot')
# Add Labels
plt.xlabel('Total Bill')
plt.ylabel('Tip')
# Show the plot
plt.show()