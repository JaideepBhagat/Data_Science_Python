import pandas as pd

df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-01','2024-01-02', '2024-01-02'],
    'City': ['NYC', 'LA', 'NYC', 'LA'],
    'Temperature': [30, 50, 27, 45],
})

pivoted = df.pivot(index='Date', columns='City', values='Temperature')
print(pivoted)
