from pyomo.environ import ConcreteModel, Var, Objective, SolverFactory

# Create the model
model = ConcreteModel()

# Define the variable with bounds
model.x = Var(bounds=(0, 3))

# Define the objective function
model.obj = Objective(expr=model.x**2, sense=1)  # sense=1 for minimization

# Solve the problem
solver = SolverFactory('glpk')  # You can install 'glpk' solver
solver.solve(model)

# Print the result
print("Optimal value of x:", model.x())
print("Minimum value of the function:", model.obj())
