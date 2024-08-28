import pandas as pd

df = pd.read_csv("data.csv")
print("Data from CSV file:\n", df)

df = pd.read_excel("data.xlsx")
print("Data from Excel file:\n", df)
