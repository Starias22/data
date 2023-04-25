import numpy as np
#slice data in an arraythat verify certain condition
arr=np.array([45,False,True,False,False],dtype=bool)
print('arr:',arr)
print("True values in arr:",arr[arr])

arr=np.array([1,2,3,4,5,6,7,8,9,10])
even=arr[arr%2==0]
print("arr:",arr)
print("Even numbers in arr:",even)

arr=np.array([1,2,-3,4,5,6,-7,8,-9,10])

neg=arr[arr<0]

print("Negative numbers in arr:",neg)
pos=arr[arr>0]
print('There are',pos.size ,'positive items in the array')
arr=np.array([1,2,3,4,5,5,5,5,-9,10])
print("There are",arr[arr==5].size,'times 5 in the array')


