import numpy as np

array_1D = np.array([1, 2, 3, 4, 5])

# Accessing elements from a 1 dimensional Array
print("Third Element:", array_1D[2])

array_2D = np.array([[1, 2, 3],[4, 5, 6]])

# Accessing elements from a 2 Dimensional array
print("Third element from second row: ", array_2D[1,2])

# Slicing a 2D array
print("All elements from second row: ", array_2D[1, :])
print("All elements in third column: ", array_2D[:, 2])

# Modifying elements
array_2D[0:3] = [10, 20, 30]
print("Modified array: ", array_2D)
