import numpy as np


"""nd array is the most important object available in python
It allows us to create and manipulate multidimentinal arrays"""

#nd array creation
"""To create an ndarray we can use the array method of numpy"""
"""It takes among others args, at least an object
That object can be a sequence(list, tuple)"""
#an array
arr=np.array([1,2,3,4])
print("arr:",arr)
print("type(arr): ",type(arr))

#another array

arr2=np.array([[1,2,3],[4,5,6]])
print("arr2:",arr2)
print("type(arr2): ",type(arr2))

#with tuple
arr3=np.array(([1,2,3],[4,5,6]))
print("arr3:",arr2)
print("type(arr3): ",type(arr3))




"""

cplx=np.array([1,2,5,7],dtype=complex)
print("complex array:",cplx)
print("cplx.ndim: ",cplx.ndim)
print("elements type:",cplx.dtype)
print("cplx.itemsize:",cplx.itemsize)
print("cplx.size:",cplx.size)
print("cplx.shape",cplx.shape)
print("len(cplx.shape)",len(cplx.shape))


arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]])
print("arr.ndim:",arr.ndim)
print("arr.itemsize:",arr.itemsize)
print("arr.size: ",arr.size)
print("arr.shape",arr.shape)
print("len(arr.shape)",len(arr.shape))

arr=np.array([[1,2,3],[4,5,6]],dtype=float)
print("arr:",arr,sep="\n")
print("type(arr)",type(arr))
print("arr.ndim: ",arr.ndim)
print("elements type:",arr.dtype)
print("arr.itemsize:",arr.itemsize)
print("arr.size: ",arr.size)
print("arr.shape",arr.shape)
print("len(arr.shape)",len(arr.shape))

arr=arr.reshape(3,2)
print("arr:",arr,sep="\n")
print("arr.size: ",arr.size)
print("arr.shape",arr.shape)
print("len(arr.shape)",len(arr.shape))

arr=np.array([[1,2,3],[4,5,6],[-2,6,-9]],dtype='int64')
print('arr[0][0]:',arr[0][0])
print('arr[1][2]:',arr[1][2])
print('type(arr[0][0])',type(arr[0][0]))

print("The maximum element:",arr.max())
print("The minimum element:",arr.min())
print("The sum of the elements:",arr.sum())
print("type(arr.sum()):",type(arr.sum()))

print("The maximum elements of columns:",arr.max(axis = 0))
print("The minimum element of rows",arr.min(axis = 1))
print("The sum of all rows",arr.sum(axis = 1))
arr=arr.sum(axis = 1)
print("type(arr.sum(axis = 1))",type(sum))
print("arr:",arr,sep="\n")
print("type(arr)",type(arr))
print("arr.ndim: ",arr.ndim)
print("elements type:",arr.dtype)
print("arr.itemsize:",arr.itemsize)
print("arr.size: ",arr.size)
print("arr.shape",arr.shape)
print("len(arr.shape)",len(arr.shape))

arr=np.array([[1,2,3],[4,5,6],[2,6,9]],dtype='int64')
sqrt=np.sqrt(arr)
print(sqrt)

a = np.array([[1,2,30],[10,15,4]])
b = np.array([[1,2,3],[12, 19, 29]])
print("Sum of array a and b\n",a+b)
print("Defference of array a and b\n",a-b)
print("Product of array a and b\n",a*b)
print("Division of array a and b\n",a/b)
print("modulo of a and b\n",a%b)
print("a**b\n",a**b)

a= np.array([[1,2,30],[10,15,4]])
b = np.array([[1,2,3],[12, 19, 29]])
print("Arrays vertically concatenated\n",np.vstack((a,b)));
print("Arrays horizontally concatenated\n",np.hstack((a,b)))


print("arr:",arr)
x=arr.ravel()
print("x:",x)
print("type(x)",type(x))
print("x.ndim",x.ndim)
lst=x.tolist()
print("lst",lst)


lst2=arr.tolist()
print("lst2",lst2)
"""




