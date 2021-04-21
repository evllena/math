import numpy as np
import scipy.linalg as la

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([2, 5, 11])
Q, R = la.qr(A)
print(Q)
print(R)
R1 = R[:2, :2]
B1 = np.dot(np.transpose(Q), B)[:2]
X1 = la.solve(R1, B1)
X = np.append(X1, 0)
print(la.norm(X))
print(X)

