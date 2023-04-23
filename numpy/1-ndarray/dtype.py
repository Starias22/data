import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print("arr:",arr)
print('dtype:',arr.dtype)
#int,float,bool,int32,int64,float32,float64,stretc
arr=np.array([[4,-6,6],[5,5,9]],dtype='float64')
print("arr:",arr)
print('dtype:',arr.dtype)
arr=np.array([[4,-6,60],[5,5,99]],dtype=str)
print("arr:",arr)
print('dtype:',arr.dtype)

#convert the dtype of an existing array: astype()
#convert from str to int
arr=arr.astype('int32')
print("arr:",arr)
print('dtype:',arr.dtype)

arr=np.array([[0.89,-95.88,0],[4.8,-9.,4]])
print("arr:",arr)
print('dtype:',arr.dtype)
arr=arr.astype('int32')

arr_int=arr.astype('int32')
print("arr_int:",arr_int)
print('dtype:',arr_int.dtype)

arr_bool=arr.astype('bool')

print("arr_boool:",arr_bool)
print('dtype:',arr_bool.dtype)

"""all the items should have the same type
but otherwise, the neccessary cast will be done
so as to have the same dtype
"""

#dtype will be string
arr_cast=np.array([1,2,'eating'])
print("arr_cast:",arr_cast)
print('dtype:',arr_cast.dtype)

#value erro will be trown if the conversion is not possible

#no blem
arr_cast=np.array([1,2,'eating'],dtype='str')
print("arr_cast:",arr_cast)
print('dtype:',arr_cast.dtype)

#problem:can't cast string to int
"""arr_cast=np.array([1,2,'eating'],dtype='int64')
print("arr_cast:",arr_cast)
print('dtype:',arr_cast.dtype)"""

print(arr)
#convert to string
arr=arr.astype(dtype='U6')
print("arr:",arr)
print('dtype:',arr.dtype)

arr=np.array([False,92,'PM'])#will be converted to string
print("arr:",arr)
print('dtype:',arr.dtype)


arr=np.array((False,92,'PM',True,False,'',' '),dtype=bool)#no blem
print("arr:",arr)
print('dtype:',arr.dtype)
#0 and 1
arr=arr.astype(int)
print(arr)#pass
arr=np.array([-20,'100','-70','69.9957'])#add True to the list causes blem
arr.astype(float)#no blem
print(arr)
arr=np.array(False)
arr=arr.astype(float)
print(arr)
arr=np.array([[0.89,-95.88,0],[4.8,-9.,4]],dtype=complex)
print(arr)
print(arr.astype(str))