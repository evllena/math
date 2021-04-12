from scipy.optimize import fsolve
import numpy as np


def equations(p):
    x, y = p
    return y - x ** 2 + 1,  np.exp(x) + x * (1 - y) - 1


x1, y1 = fsolve(equations, (1, 1))
print(x1, y1)
