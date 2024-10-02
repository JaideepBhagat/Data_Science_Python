import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Create a sample dataset
data = {'Scores': [70, 80, 90, 100, 80, 85]}
df = pd.DataFrame(data)

# Calculate the mean
mean = df['Scores'].mean()

# Calculate the median
median = df['Scores'].median()

# Calculate the mode
mode = df['Scores'].mode()[0]

# Calculate the variance
variance = df['Scores'].var()

# Calculate the standard deviation
std_dev = df['Scores'].std()

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")

# Generate a range of x values for the bell curve
x = np.linspace(min(df['Scores']) - 10, max(df['Scores']) + 10, 100)

# Plot the normal distribution (bell curve)
plt.figure(figsize=(10, 6))
#sns.kdeplot(df['Scores'], bw_adjust=0.5, label='Density', color='black')

# Plot vertical lines for mean, median, and mode
plt.axvline(mean, color='green', linestyle='--', label=f'Mean: {mean}')
plt.axvline(median, color='red', linestyle='--', label=f'Median: {median}')
plt.axvline(mode, color='blue', linestyle='--', label=f'Mode: {mode}')

# Highlight 1 standard deviation area
plt.fill_between(x, 0, norm.pdf(x, mean, std_dev),
                 where=((x >= (mean - std_dev)) & (x <= (mean + std_dev))),
                 color='yellow', alpha=0.3, label='1 Std Dev')

# Highlight 2 standard deviations area
plt.fill_between(x, 0, norm.pdf(x, mean, std_dev),
                 where=((x >= (mean - 2*std_dev)) & (x <= (mean + 2*std_dev))),
                 color='orange', alpha=0.2, label='2 Std Devs')

# Highlight 3 standard deviations area
plt.fill_between(x, 0, norm.pdf(x, mean, std_dev),
                 where=((x >= (mean - 3*std_dev)) & (x <= (mean + 3*std_dev))),
                 color='red', alpha=0.1, label='3 Std Devs')

# Labels and title
plt.title('Bell Curve with Mean, Median, Mode, and Standard Deviation')
plt.xlabel('Scores')
plt.ylabel('Density')
plt.legend()

# Show the plot
plt.show()