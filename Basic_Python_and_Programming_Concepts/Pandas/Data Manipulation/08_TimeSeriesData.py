import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SBIN.csv")

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' column as index
df.set_index('Date', inplace=True)

# Resample by week (W) and calculate mean for "CLOSE" prices
weekly_data = df['close'].resample('W').mean().round(2)


# Resample by month (M) and calculate mean for "CLOSE" prices
monthly_data = df['close'].resample('ME').mean().round(2)

print(weekly_data)
print("--------------------------")

print(monthly_data)

# Plot the data
plt.plot(weekly_data, label='Weekly')
plt.plot(monthly_data, label='Monthly')
plt.legend()
plt.show()

# Using rolling to calculate 9 and 50 day moving averages
df['9_day_MA'] = df['close'].rolling(window=9).mean()

df['50_day_MA'] = df['close'].rolling(window=50).mean()

df[['close', '9_day_MA', '50_day_MA']].plot()
plt.show()

