import numpy as np

#discrete difference
arr=np.array([10,20,15,26,45,20])

dff=np.diff(arr)

print('arr:',arr)
print('dff:',dff)

dff=np.diff(arr,n=2)

print('arr:',arr)
print('dff:',dff)

arr=arr.reshape((2,3),order='F')

dff=np.diff(arr,axis=1)

print('arr:',arr)
print('dff:',dff)