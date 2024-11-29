import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("sakshisatre/tips-dataset")

tips = pd.read_csv(os.path.join(path, "tip.csv"))

# Plot the Kernel Density Estimate of Total Bill
sns.kdeplot(tips['total_bill'],  # Total bill as input
            shade=True,  # Shade the plot
            color='g')  # Color
# Add Title
plt.title('Kernel Density Estimate of Total Bill')
# Add Labels
plt.xlabel('Total Bill')
plt.ylabel('Density')
# Show the plot
plt.show()