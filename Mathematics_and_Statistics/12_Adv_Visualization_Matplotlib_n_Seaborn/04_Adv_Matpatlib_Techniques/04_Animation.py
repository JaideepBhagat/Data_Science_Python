import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import kagglehub
import os
# Download sales data
path = kagglehub.dataset_download("rohitsahoo/sales-forecasting")
sales = pd.read_csv(os.path.join(path, "train.csv"))
# Convert Order Date to datetime
sales['Order Date'] = pd.to_datetime(sales['Order Date'], dayfirst=True)
# Aggregate sales by Order Date and Category
agg_sales = sales.groupby(['Order Date', 'Category']).sum().reset_index()
# Pivot data to have dates as rows and categories as columns
pivot_sales = agg_sales.pivot(index='Order Date', columns='Category', values='Sales').fillna(0)
# Create figure and axis
fig, ax = plt.subplots()
categories = pivot_sales.columns
lines = {category: ax.plot([], [], label=category)[0] for category in categories}
# Set up the plot
ax.set_xlim(pivot_sales.index.min(), pivot_sales.index.max())
ax.set_ylim(0, pivot_sales.values.max())
ax.set_xlabel('Order Date')
ax.set_ylabel('Sales')
ax.legend()
# Initialization function
def init():
    for line in lines.values():
        line.set_data([], [])
    return lines.values()
# Animation function
def animate(i):
    for category in categories:
        lines[category].set_data(pivot_sales.index[:i], pivot_sales[category][:i])
    return lines.values()
# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(pivot_sales), interval=200, blit=True)
# Show the plot
plt.show()