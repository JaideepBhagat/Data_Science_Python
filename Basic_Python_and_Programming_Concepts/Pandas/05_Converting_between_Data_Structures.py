# Convert python list to Numpy array
import pandas as pd
import numpy as np

python_list = [1, 2, 3, 4, 5]

np_array = np.array(python_list)

print(np_array)

# Convert Numpy array to Panda Series

pandas_series = pd.Series(np_array)

print(pandas_series)

# Convert Panda Series to DataFrame

pandas_dataframe = pd.DataFrame(pandas_series)

print(pandas_dataframe)
