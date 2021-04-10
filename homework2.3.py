import numpy as np
from matplotlib import pyplot as plt
from math import pi

fig, ax = plt.subplots(1, 3, figsize=(12, 6))
circle = plt.Circle((0, 0), 5,color='r', fill=False)
ax = plt.gca()
ax.add_patch(circle)
plt.axis('scaled')
plt.show()