# Example function f(x) = x^2
def f(x):
    return x**2

# Derivative approximation using a small change in x (h)
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

x_value = 2
print("Derivative of f(x) at x=2:", derivative(f, x_value))
