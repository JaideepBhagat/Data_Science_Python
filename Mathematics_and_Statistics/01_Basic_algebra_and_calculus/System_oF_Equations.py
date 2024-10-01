import numpy as np
import matplotlib.pyplot as plt

# Define the range for x values
x = np.linspace(0, 120, 400)

# Equation 1: 10 + 5y = 100, simplified to y = 18
y1 = 18 * np.ones_like(x)

# Equation 2: x - y = 1, simplified to y = x - 1
y2 = x - 1

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the two lines
plt.plot(x, y1, label="10 + 5y = 100 (y = 18)", color="blue")
plt.plot(x, y2, label="x - y = 1 (y = x - 1)", color="red")

# Adding labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of the System of Equations')
plt.grid(True)

# Show where the lines intersect
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Set the axis limits
plt.xlim([0, 120])
plt.ylim([0, 120])

# Show legend
plt.legend()

# Display the graph
plt.show()
