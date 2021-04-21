import numpy as np
import scipy.linalg as la

A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
B = np.array([[2, 5, 1]])
P, L, U = la.lu(A)
print(P)
print(L)
print(U)

C = np.concatenate((A, B.T), axis=1)
B = np.array([2, 5, 11])
print(np.linalg.matrix_rank(A), np.linalg.matrix_rank(C))
print(np.linalg.solve(A, B))