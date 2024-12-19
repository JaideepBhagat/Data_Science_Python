# Use libraries like Pandas:
import pandas as pd
df = pd.read_excel("Superstore.xls")
# Detecting missing values:
df.isnull().sum()
# Filling missing values:
value = 0
df.fillna(value, inplace=True)
# Dropping missing values:
df.dropna(inplace=True)
# Identifying data types:
print(df.dtypes)
# Removing duplicates:
df.drop_duplicates(inplace=True)
# Correcting inconsistent data:
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# # Descriptive statistics:
# # Measures of central tendency:
# # Mean: Average of values
# Convert sales column to numeric
df['Sales'] = pd.to_numeric(df['Sales'])
sales_mean = df['Sales'].mean()
print("Mean:", sales_mean)
# Median: Middle value
sales_median = df['Sales'].median()
print("Median:", sales_median)
# Mode: Most common value
sales_mode = df['Sales'].mode()
print("Mode:", sales_mode)

# Measures of dispersion:
# Range: Difference between max and min
print(f"Range: {df['Sales'].max() - df['Sales'].min()}")
# Variance: Measure of spread
print(f"Variance: {df['Sales'].var()}")
# Standard deviation: Average deviation from mean
print(f"Standard deviation: {df['Sales'].std()}")

# Visualizing data:
# Histogram: Histogram of values
import matplotlib.pyplot as plt
plt.hist(df['Sales'], bins=100)
plt.show()
# Box plot: Distribution of values
df['Sales'].plot(kind='box',  grid=True, figsize=(8, 6), color='blue')
plt.show()
# Kernel density plot: Density of values
import seaborn as sns
sns.kdeplot(df['Sales'])
plt.show()

# Correlation analysis:
# Show correlation matrix:
df_filtered = df[['Sales', 'Quantity', 'Discount', 'Profit']]
correlation_matrix = df_filtered.corr(numeric_only=True)
print(correlation_matrix)

# Visualize correlations using heatmaps:
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Visualization techniques:
# Scatter plot: Relationship between two variables
plt.scatter(df['Sales'], df['Quantity'])
plt.xlabel('Sales')
plt.ylabel('Quantity')
plt.show()

# Pair Plots:
# Visualize all variable relationships.
sns.pairplot(df_filtered)
plt.show()

# Feature Relationship Exploration
# Grouping and summarizing data:
grouped_data = df.groupby('Category')['Sales'].sum()
print(grouped_data)

