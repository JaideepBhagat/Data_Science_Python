import numpy as np

from Mathematics_and_Statistics.Basic_algebra_and_calculus.Derivatives import x_value

x = 2
# Exponential involve raising a base (usually e= 2.718) to the power of a given number.
y = np.exp(x)
print(y)

# Logarithm is the inverse of the exponential function.
# The logarithm of a number y is the number x such that y = e^x
x_value = np.log(y)
print(x_value)
