import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[2, 5, 1]])
C = np.concatenate((A, B.T), axis=1)
print(C)
print(np.linalg.matrix_rank(A), np.linalg.matrix_rank(C))

# Система не имеет решений, необходимо изменить вектор правой части, чтобы ранг совместной матрицы тоже был = 2

D = np.array([[0, 0, 0]])
E = np.concatenate((A, D.T), axis=1)
print(E)
print(np.linalg.matrix_rank(E))
D = np.array([0, 0, 0])
print(np.linalg.solve(A, D))