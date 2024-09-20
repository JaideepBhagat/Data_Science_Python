import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

print(df)
print("--------------------------")
# Adding a new column
df['Country'] = ['USA', 'UK', 'France']

print(df)
print("--------------------------")

# Removing a column
df.drop('Age', axis=1, inplace=True)

print(df)
print("--------------------------")

# Removing a row
df.drop(1, axis=0, inplace=True)

print(df)
print("--------------------------")

# Renaming columns
df.rename(columns={'Name': 'Employee Name','Country':'Nationality'}, inplace=True)

print(df)