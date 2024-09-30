import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[7, 8, 9], [10, 11, 12]])

# Matrix addition
result = matrix1 + matrix2
print(result)
# Output: [[ 8 10 12]
#          [14 16 18]]

# Matrix subtraction
result = matrix1 - matrix2
print(result)
# Output: [[-6 -6 -6]
#          [-6 -6 -6]]

matrix3 = np.array([[1, 2], [3, 4]])
# Matrix multiplication
result = np.dot(matrix3, matrix2)
print(result)
# Output:   [[27 30 33]
#            [61 68 75]]

# Matrix transpose
matrix4 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
transpose = matrix4.T
print(transpose)
# Output: [[1 4 7]
#          [2 5 8]
#          [3 6 9]]

# Determinant
matrix5 = np.array([[1, 2],
                    [3, 4]])
matrix5_det = np.linalg.det(matrix5)
print(matrix5_det)
# Output: -2.0

# Inverse
matrix5_inv = np.linalg.inv(matrix5)
print(matrix5_inv)
# Output: [[-2.  1.]
#          [ 1. -0.]]
