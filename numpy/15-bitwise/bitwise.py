print('binary representation of 10:',bin(10))
print('binary representation of 55:',bin(55))

import numpy as np

arr=10
print('binary representation of arr:',np.binary_repr(arr))
arr=45
print('binary representation of arr:',np.binary_repr(arr))



arr=np.array([25,10,20,36,0,1],dtype=np.uint8)
print('arr:',arr)
inv=np.invert(arr)
print('bin(arr):',np.vectorize(np.binary_repr)(arr))
print('bin(inv):',np.vectorize(np.binary_repr)(inv))
print('inv:',inv)

lshifted=np.left_shift(arr,2)
print('lshifted:',lshifted)

rshifted=np.right_shift(arr,2)
print('rshifted:',rshifted)

print('arr:',arr)
tab=np.array([20,28,96,1,3,2])
print('tab:',tab)

and_=np.bitwise_and(arr,tab)
print('tab and arr:',and_)

or_=np.bitwise_or(arr,tab)
print('tab or arr:',or_)


not_=np.bitwise_not(arr)
print('not tab:',not_)
print('bin(tab):',np.vectorize(np.binary_repr)(tab))
print('bin(not_):',np.vectorize(np.binary_repr)(not_))