import numpy as np
from mpmath import matrix
from numba.np.arraymath import array_prod

array_1D = np.array([1, 2, 3, 4, 5])
array_2D_1 = np.array([[1, 2, 3],[4, 5, 6]])
array_2D_2 = np.array([[7, 8],[9, 10],[11, 12]])

# Element-wise addition
array_sum = array_1D + 2
print(array_sum)

# Element-wise multiplication
array_prod = array_1D * 3
print(array_prod)

# Adding a scaler to a 2D array
matrix = np.array([[1,2],[3,4]])
broadcast_result = matrix +1
print(broadcast_result)

# Matrix Multiplication
array_product = np.dot(array_2D_1, array_2D_2)
array_product_alt = array_2D_1 @ array_2D_2
print("\n", array_product)
