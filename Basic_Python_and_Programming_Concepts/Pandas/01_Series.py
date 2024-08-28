import pandas as pd

nums = [5, 6, 7]

# Creating Panda Series
series = pd.Series(nums)

print(series)

# Accessing elements from Series
print("Second Element:", series[1])

# Creating Panda Series with index
series = pd.Series(nums, index = ['a','b','c'])

print(series)

# Accessing elements from Series
print("Second Element: ", series['b'])

# Creating Panda Series with dictionary
dict = {'a': 5, 'b': 6, 'c': 7, 'd': 8, 'e': 9}

series = pd.Series(dict)

print(series)

# Creating Panda Series with dictionary and index
series = pd.Series(dict, index = ['a','c','d'])

print(series)