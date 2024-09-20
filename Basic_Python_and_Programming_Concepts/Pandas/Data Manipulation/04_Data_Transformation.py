import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Age': [25, 30, 35, 28, 32, 36, 29, 33, 27, 31],
    'City': ['New York', 'London', 'Paris', 'Berlin', 'London', 'Paris', 'London', 'New York', 'Paris', 'London'],
    'Salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]}


df = pd.DataFrame(data)

print(df)
print("--------------------------")

def add_five(x):
    return x + 5


def increase_10percent(x):
    return x * 1.1


# Applying a function to a column
df['Age'] = df['Age'].apply(add_five)

print(df)
print("--------------------------")

# Creating new columns based on existing ones
df['Age_plus_5'] = df['Age'].apply(add_five)
print(df)
print("--------------------------")

# Using .map()
df['Revised_Salary'] = df['Salary'].map(increase_10percent)

print(df)
print('--------------------------')

