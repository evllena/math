import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-np.pi * 2, 2 * np.pi, 131)
plt.plot(x, np.cos(x))
plt.plot(x, 0.5 * np.cos(x - 3) + 2)
plt.plot(x, 2.5 * np.cos(x + 0.6) - 1)
plt.grid(True)
plt.show()
