import numpy as np


vector = np.random.rand(100, 2)

distances = np.sqrt(np.sum((vector[:, np.newaxis, :] - vector[np.newaxis, :, :])**2, axis=-1))
print(distances)

