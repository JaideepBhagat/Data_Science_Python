import pandas as pd
import matplotlib.pyplot as plt

# Load a sample dataset
data = pd.read_excel("Financial Sample.xlsx")

df = pd.DataFrame(data)

# Calculate the mean sales for each country and plot it

df = df.groupby(["Country"])[" Sales"].mean()

# Create a line chart

df.plot(kind="line")

plt.show()
