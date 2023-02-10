import numpy as np

A = np.random.randint(0, 10, (3, 3))
B = np.random.randint(0, 10, (3, 3))
print(A)
print(B)
equal = np.array_equal(A, B)
print("Arrays A and B are equal:", equal)
