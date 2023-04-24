import numpy as np
arr=np.array([1,2,3,4,3,6,2,4,2,1])

a=np.unique(arr)

print('arr:',arr,sep='\n')
print('a:',a,sep='\n')

a=np.array([[1,2,2,3,9],[1,4,3,5,8]])

b=np.unique(a)
print('a:',a,sep='\n')
print('b:',b,sep='\n')

b=np.unique(a,axis=None)
print('a:',a,sep='\n')
print('b:',b,sep='\n')

b=np.unique(a,axis=0)
print('a:',a,sep='\n')
print('b:',b,sep='\n')

b=np.unique(a,axis=1)
print('a:',a,sep='\n')
print('b:',b,sep='\n')

