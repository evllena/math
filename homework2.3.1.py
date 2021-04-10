import numpy as np
from matplotlib import pyplot as plt
from math import pi


circle = plt.Circle((0, 0), 5, color='r', fill=False)
ax = plt.gca()
ax.add_patch(circle)
plt.axis('scaled')
plt.grid(color='lightgray',linestyle='--')
plt.show()