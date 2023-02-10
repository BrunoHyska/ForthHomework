import numpy as np
import matplotlib.pyplot as plt

array = np.random.rand(5, 5)
normalized_array = (array - np.min(array)) / (np.max(array) - np.min(array))


# Uncomment the part below if there is the need to see the grahps

# plt.pie([np.min(normalized_array), np.max(normalized_array)], labels=[np.min(normalized_array), np.max(normalized_array)], startangle=90, counterclock=False)
# plt.axis('equal')
# plt.show()
#
# plt.bar(['min', 'max'], [np.min(normalized_array), np.max(normalized_array)])
# plt.xlabel('Value')
# plt.ylabel('Value')
# plt.show()

print("Original Array:", array)
print("Normalized Array:", normalized_array)
