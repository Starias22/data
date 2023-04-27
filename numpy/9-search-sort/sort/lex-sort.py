import numpy as np

a = np.array(['a','b','c','d','e'])

b = np.array([12, 90, 380, 12, 211])

ind = np.lexsort((a,b))

print("printing indices of sorted data")

print(ind)

print("using the indices to sort the array")

for i in ind:
    print(a[i],b[i])





