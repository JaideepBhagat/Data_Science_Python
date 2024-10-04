import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Key Characteristics of Normal Distribution
mean = 170  # Mean (μ) - average height in cm
std_dev = 10  # Standard deviation (σ) - spread of heights

# Generate random heights following a normal distribution
data = np.random.normal(loc=mean, scale=std_dev, size=1000)

# Plot the histogram of heights
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data (random heights)')

# Plot the Probability Density Function (PDF)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
pdf = norm.pdf(x, mean, std_dev)
plt.plot(x, pdf, 'k', linewidth=2, label='PDF (Theoretical)')

# Mark mean, and ±1σ, ±2σ, ±3σ using vertical lines
plt.axvline(mean, color='r', linestyle='dashed', linewidth=2, label='Mean (μ)')
plt.axvline(mean - std_dev, color='b', linestyle='dashed', linewidth=2, label='-1σ')
plt.axvline(mean + std_dev, color='b', linestyle='dashed', linewidth=2, label='+1σ')
plt.axvline(mean - 2*std_dev, color='y', linestyle='dashed', linewidth=2, label='-2σ')
plt.axvline(mean + 2*std_dev, color='y', linestyle='dashed', linewidth=2, label='+2σ')
plt.axvline(mean - 3*std_dev, color='purple', linestyle='dashed', linewidth=2, label='-3σ')
plt.axvline(mean + 3*std_dev, color='purple', linestyle='dashed', linewidth=2, label='+3σ')

plt.title('Normal Distribution of Heights')
plt.legend()
plt.show()

# Empirical Rule (68-95-99.7 rule)
within_1_sigma = norm.cdf(mean + std_dev, mean, std_dev) - norm.cdf(mean - std_dev, mean, std_dev)
within_2_sigma = norm.cdf(mean + 2*std_dev, mean, std_dev) - norm.cdf(mean - 2*std_dev, mean, std_dev)
within_3_sigma = norm.cdf(mean + 3*std_dev, mean, std_dev) - norm.cdf(mean - 3*std_dev, mean, std_dev)

print(f"Empirical Rule:")
print(f"68% of the data falls within ±1σ: {within_1_sigma*100:.2f}%")
print(f"95% of the data falls within ±2σ: {within_2_sigma*100:.2f}%")
print(f"99.7% of the data falls within ±3σ: {within_3_sigma*100:.2f}%\n")

# Z-scores
# Z-score of a value (let's assume height = 185 cm)
height = 185
z_score = (height - mean) / std_dev
print(f"The Z-score of height {height} cm is {z_score:.2f}, meaning it is {z_score:.2f} standard deviations from the mean.")

# Probability of a person being taller than 185 cm
prob_taller_than_185 = 1 - norm.cdf(height, mean, std_dev)
print(f"The probability of a person being taller than {height} cm is {prob_taller_than_185*100:.2f}%")
