# Use libraries like Pandas:
import pandas as pd
df = pd.read_csv("Mathematics_and_Statistics/13_Interactive_Visualization_with_Plotly/03_Real_World_Scenarios/Sales.csv")
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
# Scaling data:
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['Sales'] = scaler.fit_transform(df['Sales'].values.reshape(-1, 1))
# # Encoding categorical data:
# df_encoded = pd.get_dummies(df)
# # Descriptive statistics:
# # Measures of central tendency:
# # Mean: Average of values
# df['Sales'].mean()
# # Median: Middle value
# df['Sales'].median()
# # Mode: Most common value
# df['Sales'].mode()
# # Measures of dispersion:
# # Range: Difference between max and min
# print("Range: Difference between max and min")
# print(df['Sales'].max() - df['Sales'].min())