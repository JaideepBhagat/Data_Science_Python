import random

# Simulate flipping coins
def flip_coins(num_flips):
    heads = 0
    tails = 0
    for i in range(num_flips):
        if random.random() < 0.5:
            heads += 1
        else:
            tails += 1
    return heads, tails

# Test the function
num_flips = 1000
heads, tails = flip_coins(num_flips)
print(f"Number of heads: {heads}")
print(f"Number of tails: {tails}")
print(f"Total number of flips: {num_flips}")
print(f"Probability of heads: {heads / num_flips}")
print(f"Probability of tails: {tails / num_flips}")