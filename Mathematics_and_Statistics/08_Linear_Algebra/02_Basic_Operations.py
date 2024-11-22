import numpy as np
from numpy.ma.core import transpose

scaler = 2

vector1 = np.array([1, 2, 3])  # Creates a 1D array representing a vector.

scaler_addition = vector1 + scaler
print(f"Scalar Addition: {scaler_addition}")

scaler_subtraction = vector1 - scaler
print(f"Scaler Subtraction: {scaler_subtraction}")

scaler_multiplication = vector1 * scaler
print(f"Scaler Multiplication: {scaler_multiplication}")

vector2 = np.array([4, 5, 6])

addition = vector1 + vector2
print(f"Vector Addition: {addition}")

subtraction = vector2 - vector1
print(f"Vector Subtraction: {subtraction}")

multiplication = vector1 * vector2
print(f"Vector Multiplication: {multiplication}")

dot_vector = np.dot(vector1, vector2)
print(f"Vector Dot Product: {dot_vector}")

######## MATRIX OPERATIONS #####################

matrix1 = np.array([
    [1,2],
    [3,4]
])  # Creates a 2D array (matrix) with 2 rows and 2 columns.

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

matrix_addition = matrix1 + matrix2
print(f"Matrix Addition: \n{matrix_addition}")

matrix_subtraction = matrix2 - matrix1
print(f"Matrix Subtraction: \n{matrix_subtraction}")

matrix_multiplication = matrix1 * matrix2
print(f"Matrix Multiplication: \n{matrix_multiplication}")

dot_matrix = np.dot(matrix1, matrix2)
print(f"Matrix Dot Product: \n{dot_matrix}")
# Multiply rows of the first matrix by columns of the second.
# [1*5+2*7 1*6+2*8]
# [3*5+4*7 3*6+4*8]

transpose1 = matrix1.T
print(f"Transpose of Matrix 1: \n{transpose1}")
