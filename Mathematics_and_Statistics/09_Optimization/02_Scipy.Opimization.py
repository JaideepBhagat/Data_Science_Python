from scipy.optimize import minimize

# Define the function to minimize
def objective_function(x):
    return x**2 + 3*x + 2

# Call the minimize function
result = minimize(objective_function, 0)

# Print the result
print("Optimal value of x:", result.x)
print("Minimum value of the function:", result.fun)