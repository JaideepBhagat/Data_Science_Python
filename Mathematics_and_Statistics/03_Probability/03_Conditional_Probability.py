# Conditional Probability
def conditional_probability(A_given_B,  total_B):
    return A_given_B / total_B


# Example: P(Ace|Red) where aces are 2/26 in red cards
P_A_given_B = conditional_probability(2, 26)
print(f'P(Ace|Red) = {P_A_given_B}')
