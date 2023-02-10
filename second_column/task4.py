import numpy as np


matrix = np.random.rand(3, 5)
matrix = matrix - np.mean(matrix, axis=1, keepdims=True)
print(matrix)


