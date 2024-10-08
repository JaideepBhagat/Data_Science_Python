import pandas as pd

# Creating a datafrome from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

print(df)

# Accessing rows by index
print("First row:\n", df.loc[0])
print("------------------------")
print("First two rows:\n", df.loc[[0, 1]])
print("------------------------")
df = pd.DataFrame(data, index=['P1', 'P2', 'P3'])

print(df)
print("------------------------")
# Accessing rows by index
print("First row:\n", df.loc['P1'])
print("------------------------")
print("First two rows:\n", df.loc[['P1', 'P2']])
print("------------------------")

# Accessing columns
print("Name column:\n", df['Name'])
print("------------------------")
print("Name and Age columns:\n", df[['Name', 'Age']])
print("------------------------")
# Adding a new column
df['Country'] = ['USA', 'UK', 'France']

print(df)
print("------------------------")
# Deleting a column
del df['Country']

print(df)
print("------------------------")
# Adding a new row
df.loc['P4'] = ['Sarah', 28, 'London']

print(df)
print("------------------------")
# Deleting a row
df = df.drop('P4')

print(df)
