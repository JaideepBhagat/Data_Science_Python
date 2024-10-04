import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import poisson

# Set the rate parameter (λ)
lambda_param = 3

# Generate event counts (k) for plotting
k_values = np.arange(0, 15)

# Calculate Poisson probabilities for each k value
poisson_probs = poisson.pmf(k_values, lambda_param)

# Create the bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x=k_values, y=poisson_probs, color='skyblue')

# Add labels and title
plt.xlabel('Number of Events (k)', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title(f'Poisson Distribution (λ={lambda_param})', fontsize=14)

# Show the plot
plt.show()
