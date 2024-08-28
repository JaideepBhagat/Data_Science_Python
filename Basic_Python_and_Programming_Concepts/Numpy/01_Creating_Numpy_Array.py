import numpy as np
from numpy.array_api import linspace

# Create a 1D array
array_1D = np.array([1, 2 , 3, 4, 5])
print("1 Dimensional Array: \n", array_1D)

# Create a 2D array
array_2D = np.array([[1, 2, 3],[4, 5, 6]])
print("2 Dimensional array: \n", array_2D)

# Creating an array of zeroes
zeros_array = np.zeros((3,3))
print("Two dimensional array of Zeroes: \n", zeros_array)

# Creating an array of Ones
ones_array = np.ones((2, 4))
print("2D Array of Ones: \n", ones_array)

# Creating an array with a range of values
range_array = np.arange(0, 10, 2)
print("Array with range values: ", range_array)

# Creating an array with evenly spaced values
linspace_array = np.linspace(0, 1, 5)
print("Array of even spaced values: ", linspace_array)
