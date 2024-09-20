import pandas as pd

data = pd.read_csv("/home/jaideep/PycharmProjects/Data_Science_Python/Basic_Python_and_Programming_Concepts/Pandas/data.csv")
df = pd.DataFrame(data)

print(df)
print("--------------------------")

# Remove rows with missing values
df_cleaned = df.dropna().copy()
print(df_cleaned)
print("--------------------------")


# Replace missing values
df_cleaned = df.fillna(0).copy()
print(df_cleaned)