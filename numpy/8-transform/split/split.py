import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

sarr=np.split(arr,3)

print('sarr:',sarr)
print(type(sarr))
print(sarr[0])


arr = np.array([[1, 2, 3],[4, 5, 6]])

sarr=np.split(arr,2)

print('sarr:',sarr)
print(type(sarr))
print(sarr[1])

#sarr=np.split(arr,3)
