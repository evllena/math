import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 131)
k = [1, 0.5, 5]
for i in k:
    plt.plot(x, np.cos(x * i))
plt.show()
