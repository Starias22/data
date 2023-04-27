import numpy as np

arr=[9,8,9,63,-20,33,4]
print('arr:',arr,sep='\n')
print(np.sort(arr))

arr=np.asarray(arr)
print(arr)


a = np.array([[10,2,3],[4,5,6],[7,8,9]])

print('a:',a,sep='\n')
print("Sorting along the columns:")
print(np.sort(a))
print(np.sort(a,1))
print(np.sort(a,axis=1))



print("Sorting along the rows:")
print(np.sort(a, axis=0))
print(np.sort(a, 0))

a=[9,8,9,63,-20,33,4]

print('\nHeap sort:',np.sort(a,kind='heap'))
print('\nQuick sort:',np.sort(a,kind='quick'))#default
print('\nStable sort:',np.sort(a,kind='stable'))
print('\nMerge sort:',np.sort(a,kind='merge'))
