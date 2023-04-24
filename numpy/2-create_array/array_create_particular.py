import numpy as np
shape=(3,2)
zeros=np.zeros(shape)
print("zeros:",zeros)
print(zeros.shape)
print("zeros.dtype",zeros.dtype)


zeros=np.zeros(shape,dtype=int)
print("zeros:",zeros)
print("zeros.dtype",zeros.dtype)

zeros=np.zeros(shape,dtype=bool)
print("zeros:",zeros)
print("zeros.dtype",zeros.dtype)

zeros=np.zeros(shape,dtype=bool,order='F')
print("zeros:",zeros)
print("zeros.dtype",zeros.dtype)

ones=np.ones(shape,dtype='float32')
print("ones:",ones)
print("ones.dtype",ones.dtype)

ones=np.ones(shape,dtype='bool')
print("ones:",ones)
print("ones.dtype",ones.dtype)

ones=np.ones(shape,dtype='bool',order='C')
print("ones:",ones)
print("ones.dtype",ones.dtype)


arr=np.full(shape,fill_value=55,dtype=float)
print("arr:",arr)
print("arr.dtype",arr.dtype)

arr=np.full(shape,fill_value=55,dtype=float,order='F')
print("arr:",arr)
print("arr.dtype",arr.dtype)

#empty non initialized array
arr2=np.empty(shape=shape,dtype='float32')
print("arr2:",arr2)

arr2=np.empty(shape=shape,dtype='float32',order='F')
print("arr2:",arr2)
