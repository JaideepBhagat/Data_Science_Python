import random

from sympy.stats.rv import probability


# Function to simulate rolling a dice
def roll_dice():
    return random.randint(1, 6)

# Simulate rolling a dice 1000 times
rolls = [roll_dice() for _ in range(10000)]
probability_of_6 = rolls.count(6) / len(rolls)

print("Number of rolls:", len(rolls))
print("Number of 6's:", rolls.count(6))
print("Probability of getting 6:", probability_of_6)
