import pandas as pd

# Creating a datafrome from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

print(df)

# Accessing rows by index
print("First row:\n", df.loc[0])

print("First two rows:\n", df.loc[[0, 1]])

df = pd.DataFrame(data, index=['P1', 'P2', 'P3'])

print(df)

# Accessing rows by index
print("First row:\n", df.loc['P1'])

print("First two rows:\n", df.loc[['P1', 'P2']])

# Accessing columns
print("Name column:\n", df['Name'])

print("Name and Age columns:\n", df[['Name', 'Age']])

# Adding a new column
df['Country'] = ['USA', 'UK', 'France']

print(df)

# Deleting a column
del df['Country']

print(df)

# Adding a new row
df.loc['P4'] = ['Sarah', 28, 'London']

print(df)

# Deleting a row
df = df.drop('P4')

print(df)


