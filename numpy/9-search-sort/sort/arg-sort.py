import numpy as np


a = np.array([90, 29, 89, 12])

print("Original array:\n",a)

sort_ind = np.argsort(a)

print("Printing indices of sorted data\n",sort_ind)

sort_a = a[sort_ind]

print("printing sorted array")

for i in sort_ind:
    print(a[i],end = " ")

print('\n')





