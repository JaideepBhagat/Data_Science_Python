# Example function f(x) = x^2
def f(x):
    return x**2

# Derivative approximation using a small change in x (h)
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

x_value = 2
print("Derivative of f(x) at x=2:", derivative(f, x_value))

# Gradient Descent
def gradient_descent(f, x, learning_rate=0.1, num_iterations=100):
    for i in range(num_iterations):
        gradient = derivative(f, x)
        x -= learning_rate * gradient
    return x

print("Gradient Descent of f(x) at x=2:", gradient_descent(f, x_value))
