import numpy as np
import math

k, n = 0, 10
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1

print(k, n, k/n)


C = math.factorial(4)/(math.factorial(2)*math.factorial(4-2))
P = C * (1/(2**4))
print(C, P)

C1 = math.factorial(8)/(math.factorial(3)*math.factorial(8-3))
P1 = C1 * (1/(2**8))
print(C1, P1)

C2 = math.factorial(2)/(math.factorial(1)*math.factorial(2-1))
P2 = C2 * (1/(2**2))
print(C2, P2)
