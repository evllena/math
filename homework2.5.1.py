from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(0, 10, 131)
z = np.linspace(0, 10, 131)
X, Z = np.meshgrid(x, z)
y = 15 * x*x
y2 = 15 * x * x + 1500
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, y, Z)
ax.plot_surface(X, y2, Z)
plt.show()

