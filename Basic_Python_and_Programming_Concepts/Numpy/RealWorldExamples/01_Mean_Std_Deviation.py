import numpy as np

# Generate a large dataset of random numbers
data = np.random.randn(1000000)

# Calculate the mean
mean = np.mean(data)

# Calculate the standard deviation
std_dev = np.std(data)

# Calculate the variance
variance = np.var(data)

print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Variance:", variance)