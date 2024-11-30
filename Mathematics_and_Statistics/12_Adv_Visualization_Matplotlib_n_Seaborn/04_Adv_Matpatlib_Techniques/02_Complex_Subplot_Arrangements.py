import matplotlib.pyplot as plt
import numpy as np
import kagglehub
import os
import pandas as pd
# Download sales data
path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
print(path)
sales = pd.read_csv(os.path.join(path, "train.csv"))
# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
# Plot the sales data in the first subplot
axs[0, 0].plot(sales.pivot_table(index='Region', columns='Category', values='Sales', aggfunc='mean'))
axs[0, 0].set_title('Sales Data')
# Plot the bar chart in the second subplot
axs[0, 1].bar(sales['Category'], sales['Sales'])
axs[0, 1].set_title('Sales by Category')
# Plot the scatter plot in the third subplot
axs[1, 0].scatter(sales['Region'], sales['Sales'])
axs[1, 0].set_title('Sales by Region')
# Plot the histogram in the fourth subplot
axs[1, 1].hist(sales['Sales'], bins=10)
axs[1, 1].set_title('Sales Distribution')
# Adjust spacing between subplots
plt.tight_layout()
# Show the plot
plt.show()