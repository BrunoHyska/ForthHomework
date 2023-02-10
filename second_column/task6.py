import numpy as np

matrix = np.random.rand(3, 5)

rank = np.linalg.matrix_rank(matrix)
print("Matrix:")
print(matrix)
print("Rank:", rank)


