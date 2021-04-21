import numpy as np


A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([[1, 12]])


C = np.concatenate((A, B.T), axis=1)
print(C)
B = np.array([1, 12])
print(np.linalg.matrix_rank(A), np.linalg.matrix_rank(C))
print(np.linalg.lstsq(A, B))