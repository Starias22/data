import numpy as np
arr1 = np.array([1, 2, 3, 4,2,-1])
arr2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(arr1, arr2,assume_unique=True)

print(newarr)

newarr = np.setdiff1d(arr1, arr1,assume_unique=True)

print(newarr)

arr1=[[1,2,5],[5,-1,0],[4,0,8]]
arr2=np.array([1,2,3,0])

print(np.setdiff1d(arr1,arr2,assume_unique=True))
print(np.setdiff1d(arr1,arr2,assume_unique=False))