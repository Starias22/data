import numpy as np
a = np.array([[1,20],[3,-2]])
b = np.array([[3,-8],[5,4]])
dot = np.dot(a,b)
print(dot)

a = np.asarray([1,2,3,4,5,6])
mata=a.reshape(2,3)
b = np.array([7,8,9,10,11,12])
matb=b.reshape(3,2)
print("mata:",mata)
print("matb:",matb)
dot=np.dot(mata,matb)
print("mata*matb:",dot,sep='\n')

vecta = np.asarray([1,2,3,4,5,6])
vectb = np.array([7,8,9,10,11,12])
print("vecta:",a)
print("vectb:",b)
dot=np.vdot(a,b)
print("vecta.vectb:",dot)

a = np.array([1,2,3,4,5,6])
b = np.array([23,23,12,2,1,2])
inner = np.inner(a,b)
vdot=np.vdot(a,b)
print("iner(a,b): ",inner)
print("vdot(a,b): ",vdot)


a = np.asarray([1,2,3,4,5,6])
mata=a.reshape(2,3)
b = np.array([7,8,9,10,11,12])
matb=b.reshape(3,2)
print("mata:",mata)
print("matb:",matb)
#inner=np.inner(mata,matb) errorsame shape are required
vdot=np.vdot(mata,matb)


a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[23,23,12],[2,1,2],[7,8,9]])
mul = np.matmul(a,b)
print(mul)

a = np.array([[1,2],[3,4]])
print(np.linalg.det(a))

a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])
print(np.linalg.solve(a, b))

a = np.array([[1,2],[3,4]])
print("Original array:\n",a)
b = np.linalg.inv(a)
print("Inverse:\n",b)


array1=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)
array2=np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3)

result=a*b
print('**********')
print(result)
result=np.multiply(array1,array2)
print(result)

result=np.matmul(array1,array2)
print(result)

result=np.dot(array1,array2)

print(result)
"""These are the following specifications for numpy.dot:

When both a and b are 1-D (one dimensional) arrays-> Inner product of two vectors (without complex conjugation)
When both a and b are 2-D (two dimensional) arrays -> Matrix multiplication
When either a or b is 0-D (also known as a scalar) -> Multiply by using numpy.multiply(a, b) or a * b.
When a is an N-D array and b is a 1-D array -> Sum product over the last axis of a and b.
When a is an N-D array and b is an M-D array provided that M>=2 -> Sum product over the last axis of a and the second-to-last axis of b:
Also, dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])"""