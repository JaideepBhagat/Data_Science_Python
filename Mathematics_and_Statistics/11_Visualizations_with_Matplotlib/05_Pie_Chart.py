import matplotlib.pyplot as plt
import pandas as pd
from random import randint

from scipy.stats import alpha

# Pie Charts: Ideal for categorical comparisons.
# Sample data
df = pd.DataFrame({
    'Product': ['Books', 'Shoes', 'Clothing', 'Electronics', 'Furniture'],
    'Sales': [randint(10, 100) for i in range(5)]
})
# Plot the pie chart
colors = ['red', 'orange', 'yellow', 'green', 'blue']
explode = [0.1, 0, 0, 0, 0]
plt.pie(df['Sales'], labels=df['Product'], colors=colors, explode=explode, autopct='%1.1f%%', shadow=True)
# Add Title
plt.title('Pie Chart Example')
# Change background color
plt.gca().set_facecolor('#f2f2f2')
# Show the plot
plt.show()