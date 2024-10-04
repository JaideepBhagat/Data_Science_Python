import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import binom

# Parameters
n = 10  # number of trials
p = 0.5  # probability of success

# Plot the data
x = np.linspace(0, 10, 11)  # number of successes
plt.bar(x, binom.pmf(x, n, p), color='blue')
plt.title('Binomial Distribution')
plt.show()
