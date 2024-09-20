import pandas as pd

data = pd.read_excel("/home/jaideep/PycharmProjects/Data_Science_Python/Basic_Python_and_Programming_Concepts/Pandas/Financial Sample.xlsx")

df = pd.DataFrame(data)

# Group by country and calculate mean sales
countrySales = df.groupby(['Country'])['Sales'].mean().round(2)

print(countrySales)
print("--------------------------")

# Using multiple aggregate functions
countrySales = df.groupby(['Country'])['Sales'].agg(['mean', 'count', 'sum']).round(2)

print(countrySales)
print("--------------------------")

# Multi-level grouping
countryProductSales = df.groupby(['Country', 'Product'])['Sales'].mean().round(2)

print(countryProductSales)
print("--------------------------")
