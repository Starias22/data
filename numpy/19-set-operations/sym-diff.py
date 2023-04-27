import numpy as np
arr1 = np.array([1, 2, 3, 4,2,-1])
arr2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(arr1, arr2,assume_unique=True)

print(newarr)

newarr = np.setxor1d(arr1, arr1,assume_unique=True)

print(newarr)

arr1=np.array([1,2,5,5,-8,0,-8])
arr2=np.array([1,2,3,5,-1,0])

print(np.setxor1d(arr1,arr2,assume_unique=True))
print(np.setxor1d(arr1,arr2,assume_unique=False))
