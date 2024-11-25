import cvxpy as cp

# Define the variable
x = cp.Variable()

# Define the objective function
objective = cp.Minimize(x**2 + 3*x + 2)

# Define the constraints
constraints = [x >= -2]

# Formulate the problem
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve()

# Print the optimal value of x
print("Optimal value of x:", x.value)

# Print the minimum value of the function
print("Minimum value of the function:", problem.value)