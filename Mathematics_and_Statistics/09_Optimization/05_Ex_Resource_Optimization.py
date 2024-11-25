from scipy.optimize import linprog
c = [-5, -4]
A = [[1, 1]]
b = [10]
bounds = [(0, None), (0, None)]
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds)
print(result.x)
print(result.fun)