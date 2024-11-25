import numpy as np
import matplotlib.pyplot as plt


def gradient_descent(f, df, x0, learning_rate=0.1, iterations=100):
    """
    Implements gradient descent optimization algorithm.

    Parameters:
        f (function): Objective function to minimize
        df (function): Derivative of the objective function
        x0 (float): Initial starting point
        learning_rate (float): Step size
        iterations (int): Number of iterations

    Returns:
        tuple: (optimal x value, list of x values, list of function values)
    """
    x = x0
    x_history = [x]
    f_history = [f(x)]

    for i in range(iterations):
        # Compute gradient and update x
        gradient = df(x)
        x = x - learning_rate * gradient

        # Store values for visualization
        x_history.append(x)
        f_history.append(f(x))

        # Print progress
        if (i + 1) % 10 == 0:
            print(f"Iteration {i + 1}: x = {x:.4f}, f(x) = {f(x):.4f}")

    return x, x_history, f_history


# Define objective function and its derivative
def objective(x):
    """Example function to minimize: f(x) = x^2 + 2x + 1"""
    return x ** 2 + 2 * x + 1


def derivative(x):
    """Derivative of the objective function: f'(x) = 2x + 2"""
    return 2 * x + 2


# Run gradient descent
initial_x = 2.0
learning_rate = 0.1
iterations = 50

optimal_x, x_history, f_history = gradient_descent(
    objective,
    derivative,
    initial_x,
    learning_rate,
    iterations
)

# Create visualization
plt.figure(figsize=(12, 5))

# Plot 1: Function and optimization path
plt.subplot(1, 2, 1)
x_range = np.linspace(-3, 3, 100)
y_range = [objective(x) for x in x_range]
plt.plot(x_range, y_range, 'b-', label='f(x)')
plt.plot(x_history, f_history, 'ro-', label='Gradient descent path')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Optimization Path')
plt.legend()
plt.grid(True)

# Plot 2: Convergence
plt.subplot(1, 2, 2)
plt.plot(range(len(f_history)), f_history, 'g-')
plt.xlabel('Iteration')
plt.ylabel('f(x)')
plt.title('Convergence Over Time')
plt.grid(True)

plt.tight_layout()
plt.show()

# Print results
print("\nOptimization Results:")
print(f"Initial x: {initial_x}")
print(f"Optimal x: {optimal_x:.4f}")
print(f"Minimum value f(x): {objective(optimal_x):.4f}")