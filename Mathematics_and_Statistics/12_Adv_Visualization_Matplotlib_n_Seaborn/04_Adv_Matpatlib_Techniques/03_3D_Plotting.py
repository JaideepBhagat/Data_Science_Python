import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os
# Download sales data
path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
sales = pd.read_csv(os.path.join(path, "train.csv"))
# Map regions and categories to numeric codes for plotting
regions = {region: idx for idx, region in enumerate(sales['Region'].unique(), start=1)}
categories = {category: idx for idx, category in enumerate(sales['Category'].unique(), start=1)}
# Add numeric codes to the DataFrame
sales['Region Code'] = sales['Region'].map(regions)
sales['Category Code'] = sales['Category'].map(categories)
# Create 3D bar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Bar plot
for i in range(len(sales)):
    ax.bar3d(sales['Region Code'][i], sales['Category Code'][i], 0, 0.2, 0.2, sales['Sales'][i], shade=True)
# Labels
ax.set_xlabel('Region')
ax.set_ylabel('Category')
ax.set_zlabel('Sales')
# Set region labels
ax.set_xticks(list(regions.values()))
ax.set_xticklabels(list(regions.keys()))
# Set category labels
ax.set_yticks(list(categories.values()))
ax.set_yticklabels(list(categories.keys()))
# Show the plot
plt.show()