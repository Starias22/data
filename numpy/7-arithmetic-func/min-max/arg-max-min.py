import numpy as np
x = np.arange(20).reshape(4,5) + 7

print('x:',x,sep='\n')

max_index=x.argmax()
print('index of the max:',max_index)

print('The max:',x.reshape((20))[max_index])

max_indexes=x.argmax(axis=0)
print('max_indexes:',max_indexes)

print('max items:',x[max_indexes][0])

max_indexes=x.argmax(axis=1)
print('max_indexes:',max_indexes)




min_index=x.argmin()
print('index of the min:',min_index)

print('The min:',x.reshape((20))[min_index])

min_indexes=x.argmin(axis=0)
print('min_indexes:',min_indexes)

print('min items:',x[min_indexes][0])
