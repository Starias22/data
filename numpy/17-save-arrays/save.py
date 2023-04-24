import numpy as np

arr=np.array([1,2,3,4,2])
print('arr:',arr)
np.save('file.npy',arr)

larr=np.load('file.npy')
print('loaded array:',larr)

arr2=np.array([[1,20,-60,9],[1,2,3,4]])
print('arr2:',arr2,sep='\n')
np.save('file.npy',arr2)

larr=np.load('file.npy')
print('loaded array:',larr,sep='\n')

np.savez('multi.npz',arr=arr,arr2=arr2,arr3=arr2,my_arr=arr)

arrs=np.load('multi.npz')
print('arr reloaded:',arrs['arr'])

## Append

np.savez('multi.npz',**arrs,new=[1,2,3,5])

print('The file contains',len(np.load('multi.npz')),'arrays')


