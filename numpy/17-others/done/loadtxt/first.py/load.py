import numpy as np

data=np.loadtxt('file.txt')

print('loaded data:',data,sep='\n')

print(type(data))

print(data.dtype)

# the default dtype is float64
data=np.loadtxt('file.txt',dtype=float)

print('loaded data:',data,sep='\n')
print(data.dtype)
print(data.shape[0],'rows loaded')


data=np.loadtxt('file.txt',dtype=int,usecols=[0,2,4])# spec the indexes of the cols to load

print('loaded data:',data,sep='\n')
print(data.dtype)
print(data.shape[1],'columns loaded')


data=np.loadtxt('file.txt',dtype=str)

print('loaded data:',data,sep='\n')
print(data.dtype)

