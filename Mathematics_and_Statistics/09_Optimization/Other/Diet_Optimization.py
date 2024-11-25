from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory, NonNegativeReals

# Create the model
model = ConcreteModel()

# Define data for the problem
food_items = ['Rice', 'Beans', 'Milk', 'Eggs']
costs = {'Rice': 0.5, 'Beans': 1.0, 'Milk': 0.8, 'Eggs': 0.2}  # Cost per unit of food
nutrition = {
    'Calories': {'Rice': 200, 'Beans': 150, 'Milk': 120, 'Eggs': 80},
    'Protein': {'Rice': 4, 'Beans': 8, 'Milk': 6, 'Eggs': 6},
    'Vitamins': {'Rice': 2, 'Beans': 3, 'Milk': 5, 'Eggs': 1}
}
requirements = {'Calories': 2000, 'Protein': 50, 'Vitamins': 20}  # Minimum daily requirements

# Define decision variables (amount of each food item to buy)
model.food_quantities = Var(food_items, domain=NonNegativeReals)

# Define the objective function (minimize total cost)
model.total_cost = Objective(
    expr=sum(costs[item] * model.food_quantities[item] for item in food_items),
    sense=1  # Minimize
)

# Define constraints to meet nutritional requirements
model.constraints = ConstraintList()
for nutrient, min_requirement in requirements.items():
    model.constraints.add(
        sum(nutrition[nutrient][item] * model.food_quantities[item] for item in food_items) >= min_requirement
    )

# Solve the problem
solver = SolverFactory('glpk')  # Ensure GLPK solver is installed
solver.solve(model)

# Print the results
print("Optimal Food Quantities:")
for item in food_items:
    print(f"{item}: {model.food_quantities[item]():.2f} units")
print(f"Minimum Total Cost: ${model.total_cost():.2f}")
