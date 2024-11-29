import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os

# Download latest version
path = kagglehub.dataset_download("sakshisatre/tips-dataset")

tips = pd.read_csv(os.path.join(path, "tip.csv"))

# Plot the pairplot
sns.pairplot(tips, hue='sex', palette='Set1')
# Show the plot
plt.show()