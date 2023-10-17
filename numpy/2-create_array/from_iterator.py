import numpy as np
#arr = np.fromiter(it, dtype ,count=-1  means use all)
lst = [0,2,4,6]
it = iter(lst)
arr = np.fromiter(it, dtype = float)
print('arr:',arr)
print('type(arr):',type(arr))

lst=range(10)
it=iter(lst)
arr = np.fromiter(it, dtype = int,count=5)

print('arr:',arr)
print('type(arr):',type(arr))