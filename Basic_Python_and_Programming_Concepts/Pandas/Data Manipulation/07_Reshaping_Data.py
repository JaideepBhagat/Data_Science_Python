import pandas as pd

df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-01','2024-01-02', '2024-01-02'],
    'City': ['NYC', 'LA', 'NYC', 'LA'],
    'Temperature': [30, 50, 27, 45],
})

# Using pivot() function to reshape the data
pivoted = df.pivot(index='Date', columns='City', values='Temperature')
print(pivoted)
print("--------------------------")

# Using pivot_table() function to reshape the data
sales_data = pd.read_excel("Superstore.xls", sheet_name="Orders")
df = pd.DataFrame(sales_data)
# Reshape the data using pivot()
df_salespivot = df.pivot_table(index='State', columns='Segment', values='Quantity', aggfunc='count')
print(df_salespivot)
print("--------------------------")

# Using melt() function to reshape the data

melted = pd.melt(pivoted, var_name='City', value_name='Temperature')

print(melted)
print("--------------------------")

# Using stack() function to reshape the data
stacked = pivoted.stack()
print(stacked)
print("--------------------------")
stacked.to_excel("stacked.xlsx")