import numpy as np

arr=np.array([[1,2,3],[4,5,6],[-2,6,-9]],dtype='int64')

x=arr.ravel()
print('arr:',arr,sep='\n')
print('x:',x)

x=arr.ravel(order='C')
print('arr:',arr,sep='\n')
print('x:',x)

x=arr.ravel(order='F')
print('arr:',arr,sep='\n')
print('x:',x)