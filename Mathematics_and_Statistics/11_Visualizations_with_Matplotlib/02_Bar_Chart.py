import matplotlib.pyplot as plt
import pandas as pd
from random import randint

from scipy.stats import alpha

# Bar Charts: Ideal for categorical comparisons.
# Sample data
df = pd.DataFrame({
    'Product': ['Books', 'Shoes', 'Clothing', 'Electronics', 'Furniture'],
    'Sales': [randint(10, 100) for i in range(5)]
})

# Plot the bar chart with random colors for each bar
plt.bar(df['Product'], df['Sales'], color=['red', 'orange', 'yellow', 'green', 'blue'], alpha = 0.8)
# Add Title
plt.title('Bar Chart Example')
# Add Labels
plt.xlabel('Categories')
plt.ylabel('Values')
# Change background color
plt.gca().set_facecolor('#f2f2f2')
# Show the plot
plt.show()