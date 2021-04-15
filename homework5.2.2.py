import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# Для 10 вариантов получилось не наглядно,поэтому сделала до 1000

x = []
for k in range(0, 1000):
    a = 0
    for i in range(0, 10):
        a += np.random.randint(10)
    x.append(a)

num_bins = 10
n, bins, patches = plt.hist(x, num_bins)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()