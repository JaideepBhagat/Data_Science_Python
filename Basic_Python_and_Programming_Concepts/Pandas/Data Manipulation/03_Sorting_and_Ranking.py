import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Age': [25, 30, 35, 28, 32, 36, 29, 33, 27, 31],
    'City': ['New York', 'London', 'Paris', 'Berlin', 'London', 'Paris', 'London', 'New York', 'Paris', 'London']}

df = pd.DataFrame(data)

print(df)
print("--------------------------")

# Sorting data
df_sorted = df.sort_values(by='Age', ascending=True)

print(df_sorted)
print("--------------------------")

# Ranking data
df['Rank'] = df['Age'].rank(ascending=False)

print(df)
