import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# Poisson distribution with λ = 3
λ = 3  # rate parameter
data = np.random.poisson(λ, 100)

# Plot a bar plot
x = np.arange(0, 100)
y = poisson.pmf(x, λ)
plt.bar(x, data, color='lightblue')
plt.title('Poisson Distribution')
plt.show()
