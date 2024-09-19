import pandas as pd

try:
    # Load a sample dataset
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', None, 'Dave', 'Eve', 'Frank', None, 'Grace', 'Henry'],
        'Age': [25, 30, 35, None, 28, 32, 36, None, 29, 33],
        'Salary': ['50000', '60000', '70000', '80000', '90000', '100000', None, '110000', '120000', '130000'],
    }

    df = pd.DataFrame(data)
    print(df)

    # Remove rows with missing values
    df_cleaned = df.dropna().copy()

    # Convert salary column to numeric
    df_cleaned['Salary'] = pd.to_numeric(df_cleaned['Salary'])


    print("----------------------------------------")
    print(df_cleaned)
except Exception as e:
    print("Error:", e)
