import sympy as sp

# Define the symbol
x = sp.Symbol('x')

# Define the function
f = sp.sin(x)/x

# Find the limit as x approaches 0
limit = sp.limit(f, x, 0)

# Print the result
print(limit)
