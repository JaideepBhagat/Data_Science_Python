import numpy as np

A = np.array([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]])

print(A)
    # Output: [[1 2 3]
    #         [4 5 6]
    #         [7 8 9]]
    #         [10 11 12]]

# Square matrix
B = np.array([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])

print(B)
    # Output: [[1 2 3]
    #         [4 5 6]
    #         [7 8 9]]


# Identity matrix
C = np.eye(3)

print(C)
    # Output: [[1. 0. 0.]
    #         [0. 1. 0.]
    #         [0. 0. 1.]]


# Diagonal matrix
D = np.diag([1, 2, 3, 4])

print(D)
    # Output: [[1 0 0 0]
    #         [0 2 0 0]
    #         [0 0 3 0]
    #         [0 0 0 4]]