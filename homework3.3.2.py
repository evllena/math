import matplotlib.pyplot as plt
import numpy as np
azimuths = np.radians(np.linspace(0, 360, 360))
zeniths = np.linspace(0, 2.1, 20)
r, theta = np.meshgrid(zeniths, azimuths)

values = r * np.log(theta + 2)
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.contourf(theta, r, values)
plt.show()
