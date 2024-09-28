import numpy as np


# Coefficient Matrix
A = np.array([  [10, 5],
                [1, -1]])

# Constant Vector
B = np.array([100, 1])

# Solve the system of equations
result = np.linalg.solve(A, B)

print(result)
