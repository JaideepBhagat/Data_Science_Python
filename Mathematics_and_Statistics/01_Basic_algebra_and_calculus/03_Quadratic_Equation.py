import numpy as np
import matplotlib.pyplot as plt

# Define the quadratic equation: f(x) = x^2 - 4x + 3
def quadratic_function(x):
    return x**2 - 4*x + 3

# Generate a range of x values (for plotting the graph)
x = np.linspace(-2, 6, 1000)  # This will give us 400 points between -2 and 6

# Compute the y values for each x value using the quadratic function
y = quadratic_function(x)

# Plot the graph
plt.plot(x, y, label=r'$y = x^2 - 4x + 3$')

# Add labels and a title
plt.title('Graph of Quadratic Equation')
plt.xlabel('x')
plt.ylabel('y')

# Highlight the roots (x = 1 and x = 3)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.axvline(1, color='red', linestyle='--', label="Root at x = 1")
plt.axvline(3, color='blue', linestyle='--', label="Root at x = 3")

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
