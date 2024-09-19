import pandas as pd

df = pd.read_csv("us-500.csv")

# Selecting a single column
duration = df['first_name']
print(duration)

print("------------------------------------------------")
# Selecting multiple columns
selected_columns = df[['first_name', 'last_name']]
print(selected_columns)

print("------------------------------------------------")
# Selecting rows
selected_rows = df[0:9]
print(selected_rows)

print("------------------------------------------------")
# Selecting rows and columns
selected_rows_columns = df.loc[0:9, ['first_name', 'last_name']]
print(selected_rows_columns)
