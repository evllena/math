import numpy as np
import matplotlib.pyplot as plt

plt.subplot(111, polar=True)

phi = np.arange(0, 2*np.pi, 0.01)

plt.plot(phi, 1 + (np.cos(phi)))

plt.plot((5 * np.pi / 2, 3 * np.pi), (2, 2), color='r', linewidth=1.)
plt.show()