import math

num = -4

try:
    sqr_root = math.sqrt(num)
except ValueError:
    print("Error: Cannot calculate square root of a negative number")
