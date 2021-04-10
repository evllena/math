from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)

x = np.arange(-100, 100, 1)
y = np.arange(-100, 100, 1)
X, Y = np.meshgrid(x, y)

z = 1 - (0.5 * X * X - 2 * Y * X + Y * Y)

ax.plot_surface(X, Y, z)

show()