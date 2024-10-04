import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# Poisson distribution with λ = 4
λ = 3  # rate parameter

# Plot a bar plot
x = np.linspace(0, 10, 11)
y = poisson.pmf(x, λ)
plt.bar(x, y, color='blue')
plt.title('Poisson Distribution')
plt.show()
