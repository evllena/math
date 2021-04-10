import numpy as np
from matplotlib import pyplot as plt
from math import pi


u = 3
v = 0.5
a = 5
b = 1.5

t = np.linspace(0, 2*pi, 100)
plt.plot(u + a * np.cos(t), v + b * np.sin(t))
plt.grid(color='lightgray',linestyle='--')


plt.show()