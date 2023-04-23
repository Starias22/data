import numpy as np
import numpy.matlib

x=np.matlib.empty(shape=(3,4))
print('x:',x)

x=np.matlib.empty(shape=(3,2),dtype=int)
print('x:',x)

x=np.matlib.empty(shape=(3,4),order='F')
print('x:',x)

x=np.matlib.empty(shape=(3,4),order='C')
print('x:',x)


print(numpy.matlib.zeros((4,3)))


print(numpy.matlib.ones((4,3),dtype='int64'))


print(numpy.matlib.zeros((4,3),dtype=bool))

#n M k dtype order
print(numpy.matlib.eye(4))

print(numpy.matlib.eye(3,4))

print(numpy.matlib.eye(3,M=5,k=1,dtype=int))

print(numpy.matlib.identity(4, dtype = int))

print(numpy.matlib.rand(3,2))