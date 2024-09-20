import pandas as pd

data = pd.read_csv("data.csv")

df = pd.DataFrame(data)

df_cleaned = df.dropna().copy()

# Export cleaned data to Excel and CSV
df_cleaned.to_excel("data_cleaned.xlsx")

df_cleaned.to_csv("data_cleaned.csv")
