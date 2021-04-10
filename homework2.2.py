import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 131)
y1 = 3 * x + 1
y2 = (-1/3) * x + 1
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()