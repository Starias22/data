import numpy as np
arr1 = np.array([1, 2, 3, 4,2,-1])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)

arr1=[[1,2,5],[5,-1,0],[4,0,8]]
arr2=np.array([1,2,3,0])

print(np.union1d(arr1,arr2))