import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Age': [25, 30, 35, 28, 32, 36, 29, 33, 27, 31],
    'City': ['New York', 'London', 'Paris', 'Berlin', 'London', 'Paris', 'London', 'New York', 'Paris', 'London']}

df = pd.DataFrame(data)

print(df)
print("--------------------------")

def add_five(x):
    return x + 5


# Applying a function to a column
df['Age_plus_5'] = df['Age'].apply(add_five)

print(df)