import numpy as np
arr = np.array([[1,4,7], [2,5,8],[3,6,9]])
farr=arr.flatten()

print('arr:',arr,sep='\n')
print('flatten array:',farr)


farr=arr.flatten('C')
print('flatten array::',farr)

farr=arr.flatten(order='C')
print('flatten array::',farr)

farr=arr.flatten('F')
print('flatten array Fortran style::',farr)
farr=arr.flatten(order='F')
print('flatten array Fortran style::',farr)