import numpy as np

arr = np.random.rand(16, 16)
print("Original Array:")
print(arr)

block_sum = np.array([[np.sum(arr[i:i+4, j:j+4]) for j in range(0, 16, 4)] for i in range(0, 16, 4)])
print("Block-sum Array:")
print(block_sum)
