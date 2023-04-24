import numpy as np

arr=np.array([[1,2,3],[4,5,6],[-2,6,-9]],dtype='int64')



print("The sum of the elements:",arr.sum())
print("The sum of all rows",arr.sum(axis = 1))
print("The sum+20 of all rows",arr.sum(axis = 1,initial=20))
print("The sum-20 of all comuns",arr.sum(axis = 0,initial=-20))

print("The product of the elements:",arr.prod())
print("The product of all rows",arr.prod(axis = 1))
print("The product*20 of all rows",arr.prod(axis = 1,initial=20))
print("The product*-20 of all comuns",arr.sum(axis = 0,initial=-20))

ar = np.array([5, 6, 7, 8])

x = ar.cumsum()
y=ar.cumprod()

print(x)
print(y)

print(arr.cumsum())
print(arr.cumsum(axis=0))
print(arr.cumsum(axis=1))

print(arr.cumprod())
print(arr.cumprod(axis=0))
print(arr.cumprod(axis=1))


