import numpy as np
import matplotlib.pyplot as plt

def generator_function():
    for i in range(10):
        yield i

gen = generator_function()
array = np.fromiter(gen, dtype=int)
print(array)


# Uncomment the part below if there is the need to see the grahps

# plt.pie(array, labels=array)
# plt.show()
#
# plt.bar(array, array)
# plt.show()

