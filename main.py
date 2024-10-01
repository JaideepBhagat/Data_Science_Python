import numpy as np
import matplotlib.pyplot as plt

# Generating a normal distribution
data = np.random.normal(0, 1, 1000)

# Visualizing the distribution
plt.hist(data, bins=30, density=True)
plt.title('Normal Distribution')
plt.show()
