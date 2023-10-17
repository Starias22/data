import numpy as np

arr = np.array([7,9,8,5,6,4])

print("arr:",arr,sep="\n")
print("arr.shape",arr.shape)

arr=arr.reshape(3,2)
print("arr:",arr,sep="\n")
print("arr.shape",arr.shape)

arr=np.array([[1,2,3],[8,5,6]])

rarr=arr.reshape(6)
print('rarr:',rarr)
print(arr)

arr=np.array([1,2,3,8,5,6])
rarr=np.reshape(arr,(2,3))
print('rarr:',rarr)
print(arr)

rarr=arr.reshape([2,3],order='F')
print('rarr:',rarr)

rarr=arr.reshape(6)
print('rarr:',rarr)

rarr=arr.reshape((6,))
print('rarr:',rarr)

"""rarr=arr.reshape((8,))
print('rarr:',rarr)
rarr=arr.reshape((5,))
print('rarr:',rarr)
"""


