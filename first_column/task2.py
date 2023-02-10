import numpy as np
import matplotlib.pyplot as plt

array = np.random.rand(5, 5)
min_value = np.min(array)
max_value = np.max(array)


# Uncomment the part below if there is the need to see the grahps

# plt.pie([min_value, max_value], labels=[min_value, max_value], startangle=90, counterclock=False)
# plt.axis('equal')
# plt.show()
#
# plt.bar(['min', 'max'], [min_value, max_value])
# plt.xlabel('Value')
# plt.ylabel('Value')
# plt.show()

print("Array:", array)
print("Minimum value:", min_value)
print("Maximum value:", max_value)
