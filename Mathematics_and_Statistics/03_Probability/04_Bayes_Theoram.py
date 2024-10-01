# Given probabilities
P_D = 0.01          # Probability of having the disease
P_not_D = 0.99       # Probability of not having the disease
P_T_given_D = 0.90   # Probability of testing positive given you have the disease
P_T_given_not_D = 0.05 # Probability of testing positive given you don't have the disease

# Calculate the total probability of testing positive
P_T = (P_T_given_D * P_D) + (P_T_given_not_D * P_not_D)

# Apply Bayes' Theorem
P_D_given_T = (P_T_given_D * P_D) / P_T

print(f"Probability of having the disease given a positive test: {P_D_given_T:.4f}")
