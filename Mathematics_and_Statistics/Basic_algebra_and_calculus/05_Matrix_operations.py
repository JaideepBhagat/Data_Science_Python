import numpy as np

# Define two matrices
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Matrix addition
C = A + B
print(C)
print("---------------")

# Matrix subtraction
D = A - B
print(D)
print("---------------")

# Matrix multiplication
E = np.dot(A, B)
print(E)
print("---------------")

# Matrix multiplication
F = A @ B
print(F)
print("---------------")