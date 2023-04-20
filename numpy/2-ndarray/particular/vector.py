import numpy as np
#vectors
"""Vectors arre ndarray with ndim=1 ie an 1D array
They have no colomn column"""

#Examples

vect=np.array([4,-2,-3,9,15,48])
print('vect:',vect)
print('type(vect): ',type(vect))#ndarray
print('ndim: ',vect.ndim)
print("shape: ",vect.shape)

#iterate
for elt in vect:
    print("elt",elt)

print('The vector contains ',len(vect),'elements')
if(len(vect)==vect.size):
    print('Of course')

print('first element: ',vect[0])
print('last element: ',vect[-1])
print('3rd element: ',vect[2])
print('the predecessor of the last element:',vect[-2])

print('type(vect[0])',type(vect[0]))
print('dtype:',vect.dtype)
