import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("sakshisatre/tips-dataset")

tips = pd.read_csv(os.path.join(path, "tip.csv"))

# Plot the bar plot with statistical estimates
sns.barplot(x='day',  # Day index as x-axis
            y='total_bill',  # Total bill as y-axis
            data=tips,  # Data source
            ci='sd',  # Confidence interval (standard deviation)
            palette= 'pastel')  # Color palette
# Add Title
plt.title('Bar Plot with Statistical Estimates')
# Add Labels
plt.xlabel('Day')
plt.ylabel('Total Bill')
# Change background color
plt.gca().set_facecolor('#f2f2f2')
# Show the plot
plt.show()
