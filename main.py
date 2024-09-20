import pandas as pd

df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
df2 = pd.DataFrame({'Name': ['Charlie', 'David'], 'Age': [35, 40]})

result = pd.concat([df1, df2], ignore_index=True)
print(result)
