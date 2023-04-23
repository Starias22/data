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






