import pandas as pd
import numpy as np

data = {'A':[1, 2, 3], 'B':[4, 5, 6]}

df = pd.DataFrame(data)

# Use numpy function within pandas
df['C'] = np.sqrt(df['A']**2 + df['B']**2)

print(df)
