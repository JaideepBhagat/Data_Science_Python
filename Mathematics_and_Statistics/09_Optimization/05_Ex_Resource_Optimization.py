import cvxpy as cp

# Define the variables
x = cp.Variable(nonneg=True)
y = cp.Variable(nonneg=True)

# Define the constraints
constraints = [x + y <= 10]  # x + y <= 10

# Define the objective function: Maximize 5*x1 + 4*x2
objective = cp.Maximize(5*x + 4*y)

# Formulate the problem
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve()

# Output the results
print("Optimal variable values:")
print(f"x = {x.value}")
print(f"y = {y.value}")
print(f"Optimal function value = {problem.value}")
