import statsmodels.api as sm
import pandas as pd

# Multiple factors for predicting stock returns
X = pd.DataFrame({
    'Market_Returns':[1, 2, 3, 4, 5],
    'Size':[10, 20, 30, 40, 50],
    'Book to Market':[0.5, 0.6, 0.7, 0.8, 0.9]
})

Y = [1.5, 2.5, 3.5, 4.5, 5.5]  # Stock Returns

X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print(model.summary())