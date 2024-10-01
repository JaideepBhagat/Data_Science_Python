import sympy as sp

# Define the variables
a, b = sp.symbols('a b')

# Define the function f(a, b)
f = a**2 + 2*a*b + b**2

# Compute the partial derivative with respect to a
partial_derivative_a = sp.diff(f, a)

# Compute the partial derivative with respect to b
partial_derivative_b = sp.diff(f, b)

# Print the results
print("Partial derivative of f(a, b) with respect to a:", partial_derivative_a)
print("Partial derivative of f(a, b) with respect to b:", partial_derivative_b)
