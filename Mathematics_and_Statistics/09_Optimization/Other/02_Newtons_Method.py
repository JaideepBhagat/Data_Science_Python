import numpy as np
import matplotlib.pyplot as plt


def newtons_method(f, df, ddf, x0, iterations=20):
    """
    Implements Newton's Method for optimization.

    Parameters:
        f (function): Objective function
        df (function): First derivative
        ddf (function): Second derivative (Hessian in 1D)
        x0 (float): Initial point
        iterations (int): Maximum iterations

    Returns:
        tuple: (optimal x, history of x values, history of function values)
    """
    x = x0
    x_history = [x]
    f_history = [f(x)]

    for i in range(iterations):
        # Newton's update step: x = x - f'(x)/f''(x)
        first_derivative = df(x)
        second_derivative = ddf(x)

        # Check if second derivative is too close to zero
        if abs(second_derivative) < 1e-10:
            print("Warning: Second derivative close to zero. Stopping.")
            break

        # Newton's update
        x = x - first_derivative / second_derivative

        # Store history
        x_history.append(x)
        f_history.append(f(x))

        # Print progress
        if (i + 1) % 5 == 0:
            print(f"Newton Iteration {i + 1}: x = {x:.6f}, f(x) = {f(x):.6f}")

    return x, x_history, f_history


def gradient_descent(f, df, x0, learning_rate=0.1, iterations=50):
    """
    Implements Gradient Descent for comparison.
    """
    x = x0
    x_history = [x]
    f_history = [f(x)]

    for i in range(iterations):
        x = x - learning_rate * df(x)
        x_history.append(x)
        f_history.append(f(x))

        if (i + 1) % 10 == 0:
            print(f"GD Iteration {i + 1}: x = {x:.6f}, f(x) = {f(x):.6f}")

    return x, x_history, f_history


# Define test function and its derivatives
def f(x):
    """Example function: f(x) = x^4 - 4x^2 + 2"""
    return x ** 4 - 4 * x ** 2 + 2


def df(x):
    """First derivative: f'(x) = 4x^3 - 8x"""
    return 4 * x ** 3 - 8 * x


def ddf(x):
    """Second derivative: f''(x) = 12x^2 - 8"""
    return 12 * x ** 2 - 8


# Initial point and parameters
x0 = 2.0

# Run both methods
newton_x, newton_x_hist, newton_f_hist = newtons_method(f, df, ddf, x0)
gd_x, gd_x_hist, gd_f_hist = gradient_descent(f, df, x0)

# Visualization
plt.figure(figsize=(15, 5))

# Plot 1: Function and optimization paths
plt.subplot(1, 2, 1)
x_range = np.linspace(-2.5, 2.5, 200)
y_range = [f(x) for x in x_range]
plt.plot(x_range, y_range, 'b-', label='f(x)')
plt.plot(newton_x_hist, [f(x) for x in newton_x_hist], 'ro-',
         label='Newton\'s Method', markersize=4)
plt.plot(gd_x_hist, [f(x) for x in gd_x_hist], 'go-',
         label='Gradient Descent', markersize=4)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Optimization Paths Comparison')
plt.legend()
plt.grid(True)

# Plot 2: Convergence comparison
plt.subplot(1, 2, 2)
plt.semilogy(range(len(newton_f_hist)),
             [abs(f - min(newton_f_hist)) for f in newton_f_hist],
             'r-', label='Newton\'s Method')
plt.semilogy(range(len(gd_f_hist)),
             [abs(f - min(gd_f_hist)) for f in gd_f_hist],
             'g-', label='Gradient Descent')
plt.xlabel('Iteration')
plt.ylabel('log(Error)')
plt.title('Convergence Comparison')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Print final results
print("\nFinal Results:")
print(f"Newton's Method - Final x: {newton_x:.6f}, f(x): {f(newton_x):.6f}")
print(f"Gradient Descent - Final x: {gd_x:.6f}, f(x): {f(gd_x):.6f}")