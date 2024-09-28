import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y = (5 - 2*x) / 3

plt.plot(x, y, label="2x + 3y = 5")
plt.axhline(0, color='black',linewidth=0.25)
plt.axvline(0, color='black',linewidth=0.25)
plt.grid(True)
plt.legend()
plt.show()
