import pandas as pd

# Using pivot() function to reshape the data

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Age': [25, 30, 35, 28, 32, 36, 29, 33, 27, 31],
    'City': ['New York', 'London', 'Paris', 'Berlin', 'London', 'Paris', 'London', 'New York', 'Paris', 'London']}

df = pd.DataFrame(data)

# Reshape the data using pivot()
df_pivot = df.pivot(index='Name', columns='City', values='Age')
print(df_pivot)
print("--------------------------")

# Using pivot_table() function to reshape the data
sales_data = pd.read_excel("Superstore.xls", sheet_name="Orders")
df = pd.DataFrame(sales_data)
# Reshape the data using pivot()
df_salespivot = df.pivot_table(index='State', columns='Segment', values='Quantity', aggfunc='sum')
print(df_salespivot)
print("--------------------------")

# Using melt() function to reshape the data

melted = pd.melt(df_salespivot, var_name='Segment', value_name='Quantity')

print(melted)
print("--------------------------")

# Using stack() function to reshape the data
stacked = df.stack()
print(stacked)
print("--------------------------")
stacked.to_excel("stacked.xlsx")