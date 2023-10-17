import numpy as np

arr=np.array([1,8,37,9,8,9,6,3,2,1,4,5])

# the 2 required args
rarr=np.resize(a=arr,new_shape=12)
print('rarr shape=12:',rarr)

rarr=np.resize(a=arr,new_shape=5)
print('rarr shape=5:',rarr)

rarr=np.resize(a=arr,new_shape=15)
print('rarr shape=15:',rarr)

rarr=np.resize(arr,(4,3))
print('rarr shape=(4,3):',rarr,sep='\n')

rarr=np.resize(arr,(2,3))
print('rarr shape=(2,3):',rarr,sep='\n')

rarr=np.resize(arr,(4,4))
print('rarr shape=(4,4):',rarr,sep='\n')

