import numpy as np
a = np.array([[10,2,3],[4,5,6],[7,8,9]])

print('a:',a)
print("Sorting along the columns:")
print(np.sort(a))
print(np.sort(a,1))
print(np.sort(a,axis=1))



print("Sorting along the rows:")
print(np.sort(a, axis=0))
print(np.sort(a, 0))

print(np.sort(a,kind='heap'))
print(np.sort(a,kind='quick'))#default
print(np.sort(a,kind='stable'))
print(np.sort(a,kind='merge'))

a = np.array([90, 29, 89, 12])

print("Original array:\n",a)

sort_ind = np.argsort(a)

print("Printing indices of sorted data\n",sort_ind)

sort_a = a[sort_ind]

print("printing sorted array")

for i in sort_ind:
    print(a[i],end = " ")

a = np.array(['a','b','c','d','e'])

b = np.array([12, 90, 380, 12, 211])

ind = np.lexsort((a,b))

print("printing indices of sorted data")

print(ind)

print("using the indices to sort the array")

for i in ind:
    print(a[i],b[i])





