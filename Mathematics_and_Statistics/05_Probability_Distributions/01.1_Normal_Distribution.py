import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate random numbers from a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)

# Plot the data
plt.hist(data, bins=30, density=True, alpha=0.6, color='b')

# Setup plotting the Normal Distribution
xmin, xmax = plt.xlim()  # get the range of x values
x = np.linspace(xmin, xmax, 100)  # create an array of x values
p = norm.pdf(x, 0, 1)  # calculate the probability density function
plt.plot(x, p, 'red', linewidth=2)
plt.title('Normal Distribution')
plt.show()
