import numpy.random as rd

arr=['mango','pineapple','orange','apple']

print('arr at the beginning:',arr)

rd.shuffle(arr)#return None

print('arr after permuation:',arr)

arr=['mango','pineapple','orange','apple']

pm=rd.permutation(arr)
print('Permutted array:',pm)
print('arr after permuation:',arr)






