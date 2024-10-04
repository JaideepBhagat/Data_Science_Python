import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# Poisson distribution with λ = 3
λ = 3  # rate parameter

# Plot a bar plot
x = np.arange(0, 15)
y = poisson.pmf(x, λ)
plt.bar(x, y, color='lightblue')
plt.title('Poisson Distribution')
plt.show()
