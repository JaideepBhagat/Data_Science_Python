import statsmodels.api as sm

# Example data for bond prices and interest rates
X = [1, 2, 3, 4, 5, 6, 7, 8]  # interest rates
Y = [100, 95, 90, 85, 80, 75, 70, 65]  # bond prices

X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print(model.summary())