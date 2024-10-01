import numpy as np
import matplotlib.pyplot as plt

# Define the linear equation: 2x + 3y = 5
x = np.linspace(-5, 5, 100)
y = (5 - 2*x) / 3

# Plot the graph
plt.plot(x, y, label="2x + 3y = 5")
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True)
plt.legend()
plt.show()
