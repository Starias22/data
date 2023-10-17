import numpy as np

#length:the number of elements inside
"""
When we want to create an ndarray we use the array method and specifiate
0 or  one sequence(list,tuple or array)
the number of elements(sequences or simple elements) in that sequence is it length
an array"""
arr=np.array([1,2,3,4])
print("arr:",arr)
print("type(arr): ",type(arr))
print("arr contains ",len(arr),'elements')

#another array

arr2=np.array([[1,2,3],[4,5,6]])
print("arr2:",arr2)
print("type(arr2): ",type(arr2))
print("arr2 contains ",len(arr2),'elements')

#with tuple
arr3=np.array(([1,2,3],[4,5,6]))
print("arr3:",arr3)
print("type(arr3): ",type(arr3))
print("arr3 contains ",len(arr3),'elements')



#the number of dimension(s):ndim
"""It is the number of opening(or enclosing) remote brackets at it declaration """
#the type of an item(or data):dtype


#examples
arr0D=np.array(8)
print("arr0D:",arr0D)
print("type(arr0D): ",type(arr0D))
#print("arr0D contains ",len(arr0D),'elements')

#vector or 1-D array
"""arrays whose elements are simple data(integer,float,string,etc)"""
arr1D=np.array([1,5,6])
print("arr1D:",arr1D)
print("type(arr1D): ",type(arr1D))
print("arr1D's sequecne contains ",len(arr1D),'elements')

#matrix or 2-D array: the most used
"""arrays whose rows(elements) are 1D arrays(vectors)"""

arr2D=np.array([[45,-20,66],[5,9,6]])
print("arr2D:",arr2D)
print("type(arr2D): ",type(arr2D))
print("arr2D's sequence contains ",len(arr2D),'elements')

#another matrix or 2-D array
arr2D2=np.array([[45,-20.8,66],[5,9,6],[4,5,6.8]])
print("arr2D2:",arr2D2)
print("type(arr2D2): ",type(arr2D2))
print("arr2D2's sequence contains ",len(arr2D2),'elements')


#3-D array
"""arrays whose rows(elements) are 2D arrays(matrixes)"""
arr3D=np.array([
   [[5,-2.8,66],[5,9.20,6],[4,5.55,6.8]],
   [[45,-20.4,66],[5,200,6],[4,856,6.8]],
   [[45,-10.8,66],[5,9,6],[4,5,7.8]]
   ])
print("arr3D:",arr3D)
print("type(arr3D): ",type(arr3D))
print("arr3D's sequence contains ",len(arr3D),'elements')


#data type:dtype
"""It's the type of each data of the ndarray"""
# the size of an item:itemsize
"""it's the memory space in bytes, allocated to each element of
the ndarray"""

#the array shape: shape
"""It is a tuple of all the dimensions of the array
It lenght equals the number of dimensions of the array."""
# the size of the array:size
"""it is the number of item in the array
It is equal to the product of all items in the shape
"""

#scalar or 0-D array
"""arrays  with a single elemnt(integer,float,string,etc)"""

a=np.array([[1,2,3],[4,5,6]])
b = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]])
c= np.array([[1,2,30],[10,15,4]])
d = np.array([[1,2,3],[12, 19, 29]])
lx=np.array([1,2,5.8,7])
e=np.array([True,False,False,True])

def properties(arr):
    print('array:',arr)
    print('ndim:',arr.ndim)
    print('shape:',arr.shape)
    print('dtype:',arr.dtype)
    print('itemsize:',arr.itemsize)
    print('*****\n\n\n\n*****')


properties(a)
properties(b)
properties(c)
properties(d)
properties(e)
properties(lx)
properties(arr)
properties(arr2)
properties(arr3)
properties(arr0D)
properties(arr1D)
properties(arr2D)
properties(arr2D2)
properties(arr3D)
properties(arr2)
properties(arr3)



