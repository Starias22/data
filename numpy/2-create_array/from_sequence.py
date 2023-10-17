import numpy as np
#create ndarray from an existing sequence(list or tuple)
#arr=np.asarray(lst,dtype=,order='C')
lst=[5,6,-9,7]

arr=np.asarray(lst)
print("arr:",arr)
tup=tuple(lst)
print('tup:',tup)
arr2=np.array(tup)

arr=np.array(lst,order='F')
print("arr:",arr)
print(arr.shape)

arr=np.asarray([[1,2,3,4],[5,6,8,-9]])
print("arr:",arr)
print(arr.shape)

lst=[[1,2,3,4],[5,6,8,-9]]
arr=np.asarray(lst,dtype=float,order='C')
print("arr:",arr)
print(arr.shape)

arr=np.asarray(lst,dtype=float,order='F')
print("arr:",arr)
print(arr.shape)

l=[[1,2,3,4,5,6,7],[8,9]]
a = np.asarray(l,dtype=object);
print(type(a))
print(a)
