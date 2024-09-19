import pandas as pd

data1 = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']}

data2 = {'Name': ['Dave', 'Eve', 'Frank'],
         'Age': [28, 32, 36],
         'City': ['Berlin', 'Paris', 'London']}


# Merging two dataframes
df1 = pd.DataFrame(data1, index=['P1', 'P2', 'P3'])
df2 = pd.DataFrame(data2, index=['P4', 'P5', 'P6'])

df = pd.concat([df1, df2])

print(df)
print("--------------------------------------")
# Grouping data by a columnn
grouped = df.groupby('City')['Age'].mean()
print("Grouped data:\n", grouped)


