import numpy as np
arr=np.array([1,6,9,10,45])
print('arr:',arr)
print('ndim:',arr.ndim)
print('first element',arr[0])
print('last element',arr[-1])
print('third element',arr[2])
print('arr[-2]',arr[-2])
#index error when tryin to access an index out of bound
"""arr[20]
arr[-10]"""
#change the 4th element
arr[3]=-56
#change thelast element
arr[-1]=967
print('Array after update:',arr)
#update doesn't lead to dtype chaning
"""So if the new data is not as the same type as the dtype,
it try to cast the data to the dtype
"""
arr[4]=45.58#45 will be used instead
"""ValueError if the cast fails"""
#for example
#arr[4]='error'

print('Array after update:',arr)
for elt in arr:
    print(elt)
print(type(arr[0]))
if type(arr[0])==arr.dtype:
    print("Of course")

scal=np.array(56)
print(scal)
print('dtype:',scal.dtype)
print('ndim:',scal.ndim)
print('shape:',scal.shape)
scal=58
print(scal)
#but we cannot index an OD array:typeError
#scal[0]
#we can assin a scal to a data of vector
arr[2]=scal
print(arr)
#extract from index 1 to index 2
x=arr[0:3]
print('x',x)
print('type(x)',type(x))
print('ndim:',x.ndim)
#slice from index 1 to index -2(the elt before the last one)
x=arr[1:-1]
print(x)
#slice from index 1 to index -2(the elt before the last one)
x=arr[1:len(arr)]#extract from inde 1 to the last data the array
x=arr[2:arr.size]#extract from index 2 to the last data the array
print(x)
#index erro is not raised when the second index of the slice exed
"""It simply arrest at the end"""
print(arr[1:90])
#the first elt should be grater than
print(arr[2:1])#no element
print(arr[2:2])#no element
#assign
arr[2:-1]=20
print(arr)

#extract from index 1 to the end
y=arr[1:]
print(y)
z=arr[:3]#from the begining to index 2
print(z)
arr[:4]=-20
print(arr)
arr[:-2]=-100#from the beg to elt before the one before the last one

#step
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)
#slice from index 3 to index 10 with the step 2
u=arr[3:11:2]
print(u)


#slice from index 0 to index 10 with the step 3
u=arr[:11:3]
print(u)
#slice from index 3 to the end with the step 4
u=arr[3: :4]
print(u)

#slice all elements with step 3
u=arr[: :3]
print(u)

#step cannot be zero
#negative step

#slice all elements with step 2 from end to beg(reverse order)
u=arr[::-2]
print(u)

#slice all elements with step 1 from end to beg(reverse order)
u=arr[::-1]
print(u)
arr[::-3]=924
print(arr)

