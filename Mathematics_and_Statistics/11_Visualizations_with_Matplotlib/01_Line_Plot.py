import matplotlib.pyplot as plt
import pandas as pd

# Line Plots: Best for trends over time.
# Sample data
df = pd.DataFrame({
    'years': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'sales': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
})

# Plot the line
plt.plot(df['years'], df['sales'], marker='o', color='blue', linestyle='--')
# Add Title
plt.title('Sales Growth over years')
# Add Labels
plt.xlabel('Years')
plt.ylabel('Sales')
# Show Grid
plt.grid(True)
# Change background color
plt.gca().set_facecolor('#f2f2f2')
# Show the plot
plt.show()