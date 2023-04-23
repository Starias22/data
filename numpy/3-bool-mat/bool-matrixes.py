import numpy as np

arr=np.array([20,69,-20,45,-15,66,-96,0,-26,0])
#x is a matrix of bool  with the same size and ndim with arr containing
#for each data, True if the one at the same
# index in arr is positive and False else
# == > >= <=
x=arr>0
print(x)
print(type(x))
print(arr==0)
print(arr%3==0)
print(arr<=0)

arr=np.array([[1,0,0,4],[-2,-1,-5,-4],[-9,-6,-7,0]])
print(arr>=0)
print(arr<0)
arr=arr.astype(str)
print(arr)
print(arr.astype(float)>0)
arr=arr.astype(np.int64)
print(arr+5==10)
print(arr/8<9)
print(arr*2>77)
print(arr//3<9)
mat=((arr//3<9) | (arr+5==10))
print(mat)

mat=((arr%2==0) | (arr%3==0))
print(mat)

vect1=np.arange(start=1,stop=11)
print('vect1:',vect1)
vect2=np.array([5,6,1,3,-9,-6,1,45,9,4])
print('vect2:',vect2)
print(vect1>vect2)


