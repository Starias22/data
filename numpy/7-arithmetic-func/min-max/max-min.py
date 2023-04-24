import numpy as np

arr=np.array([[1,2,3],[4,5,6],[-2,6,-9]],dtype='int64')

print("The maximum element:",arr.max())
print("The minimum element:",arr.min())


print("The maximum elements of columns:",arr.max(axis = 0))
print("The minimum element of rows",arr.min(axis = 1))
