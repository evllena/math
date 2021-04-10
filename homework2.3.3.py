from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0.1, 10, 131)
y1 = 2 / x
y2 = -2 / x
plt.plot(x, y1, color='r')
plt.plot(-x, y2, color='r')
plt.grid(color='lightgray',linestyle='--')
plt.show()