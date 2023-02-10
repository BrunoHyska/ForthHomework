import numpy as np
import matplotlib.pyplot as plt

vector = np.arange(10, 50)
reversed_vector = np.fliplr([vector])[0]


# Uncomment the part below if there is the need to see the grahps

# plt.pie(vector, labels=vector, startangle=90, counterclock=False)
# plt.axis('equal')
# plt.show()
#
# plt.bar(np.arange(len(vector)), vector)
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.show()

print("Original vector:", vector)
print("Reversed vector:", reversed_vector)

