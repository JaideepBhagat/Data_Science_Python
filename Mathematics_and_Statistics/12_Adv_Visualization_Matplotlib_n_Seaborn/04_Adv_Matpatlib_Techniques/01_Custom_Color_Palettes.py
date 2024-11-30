import matplotlib.pyplot as plt
# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
# Define custom color palette
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
# Plot the bar chart with custom colors
plt.bar(categories, values, color=colors)
plt.title('Custom Color Palette')
plt.show()