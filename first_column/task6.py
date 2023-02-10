import numpy as np

rand_array = np.random.uniform(5, 15, 10)

int_array_1 = np.floor(rand_array)
int_array_2 = rand_array.astype(int)
int_array_3 = np.round(rand_array)
int_array_4 = np.trunc(rand_array)
int_array_5 = np.int_(rand_array)

print("Random Array:", rand_array)
print("Integer Array using numpy.floor:", int_array_1)
print("Integer Array using numpy.trunc:", int_array_2)
print("Integer Array using numpy.around:", int_array_3)
print("Integer Array using numpy.rint:", int_array_4)
print("Integer Array using numpy.astype:", int_array_5)
