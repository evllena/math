import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)

x = np.arange(-100, 100, 1)
y = np.arange(-100, 100, 1)
X, Y = np.meshgrid(x, y)
z2 = (X**2)/3-(Y**2)/2
ax.plot_surface(X, Y, z2)

show()