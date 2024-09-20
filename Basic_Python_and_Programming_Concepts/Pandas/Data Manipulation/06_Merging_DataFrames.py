import pandas as pd

ordersData = pd.read_excel("Superstore.xls", sheet_name="Orders")

returnsData = pd.read_excel("Superstore.xls", sheet_name="Returns")

# Merging two dataframes
mergedData = pd.merge(ordersData, returnsData, on="Order ID", how="outer")

print(mergedData)

