import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([8, 13])

# Solving linear equations
x, y = np.linalg.solve(A, B)
print(f"x = {x} and y = {y}")

###############################
A = np.array([
    [2, 1],
    [1, 2]
])

λ, v = np.linalg.eig(A)
print(f"Eigen Values: \n{λ} \nEigen Vectors: \n{v}")

############# MATRIX DECOMPOSITION #######################

# Singular Value Decomposition
U, S, V = np.linalg.svd(A)
print(f"Left singular vectors:\n{U}\nSingular values:\n{S}\nRight singular vectors:\n{V}")

