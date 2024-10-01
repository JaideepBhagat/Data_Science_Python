import numpy as np
from scipy.integrate import quad


def f(x):
    return x**2


result, error = quad(f, 0, 2)
print(result)
