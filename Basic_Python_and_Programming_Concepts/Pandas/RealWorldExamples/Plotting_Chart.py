import pandas as pd
import matplotlib.pyplot as plt

# Load a sample dataset
data = pd.read_excel("Financial Sample.xlsx")

df = pd.DataFrame(data)

# Plot the data
df.plot(x="Country", y="Sales", kind="bar")
plt.title("Sales by Country")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.show()