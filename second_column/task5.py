import numpy as np
import matplotlib.pyplot as plt


array = np.random.rand(10, 4)

sorted_array = array[array[:,1].argsort()]
print(sorted_array)

# Bar plot
plt.bar(range(len(sorted_array[:,1])), sorted_array[:,1])
plt.show()
