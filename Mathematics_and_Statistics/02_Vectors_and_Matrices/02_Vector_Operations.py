import numpy as np

# Define two vectors
vector_1 = np.array([1, 2, 3])
vector_2 = np.array([4, 5, 6])

# Vector addition
add = vector_1 + vector_2
print(add)  # Output: [5, 7, 9]

# Vector subtraction
sub = vector_1 - vector_2
print(sub)  # Output: [-3, -3, -3]

# Scalar multiplication
scalar = 2 * vector_1
print(scalar)  # Output: [2, 4, 6]

# Dot product
dot_product = np.dot(vector_1, vector_2)
print(dot_product)  # Output: 32

# Magnitude of a vector
magnitude = np.linalg.norm(vector_1)
print(magnitude)  # Output: 3.7416573867739413

# Normalize a vector
normalized_vector = vector_1 / magnitude
print(normalized_vector)  # Output: [0.26726124, 0.53452248, 0.80178373]