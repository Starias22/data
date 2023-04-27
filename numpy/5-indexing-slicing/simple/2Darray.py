import numpy as np
arr=np.array([[1,2,3],[4,5,6],[-2,6,-9]],dtype='int64')

#elements indexing

#first row, last column
print('arr[0][0]:',arr[0][0])
#second row(at index1), colum at index 2(third column)
print('arr[1][2]:',arr[1][2])
#type of data
print('type(arr[0][0])',type(arr[0][0]))
if type(arr[0][0])==arr.dtype:
    print("Of course")
#first row, last column
print('arr[0,0]:',arr[0,0])
print('arr[1,2]:',arr[1,2])

#first row, last column
print('arr[0][-1]:',arr[0][-1])

#last row, column at index2
print('arr[-1,2]:',arr[-1,2])
#last row, last column
print('arr[-1,-1]:',arr[-1,-1])

arr[1][2]=20
arr[2,2]=-60
arr[-1,-1]=55
print(arr)
#vectors indexing

#rows s
#browse the elements of the array
for elt in arr:
    print("elt:",elt)

first=arr[0]#first row of the array
print("first element:",first)
print("type(first):",type(first))
print("first.shape",first.shape)
if first.ndim==1:
    print("first is a 1D array(a vector)",first,
        "with",first.shape[0],"elements")

second=arr[1]#second row of the array
print("second element:",second)
last=arr[-1]# or arr[2]:last row of the array
print("last element:",last)

#for example get all the data(entries) of an array in a list
def getData(arr):
    lst=list()
    for i in range(arr.shape[0]):#browse the row
        for j in range(arr.shape[1]):##browse the column
            lst.append(array[i,j])#add data to the list
    return lst
array=np.array([ [1,5,6,8],[1,-5,6,9],[8,58,16,88]])
lst=getData(array)
print("entries in array: ",lst)

print('array[1]',array[1])
#we can assin vector at an index of 2D array
vect=np.arange(-16,stop=-12)
print(vect)
#assignment
array[1]=vect
print(array)

#we can assing a scalor as data to an 2D array
array[1,2]=np.array(-600)
print(array)

#all data in the first row equal 1
array[0]=1
#all data in the  row before the last one equal -1
array[-2]=-1
print(array)




#slicing

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print('arr:',arr,sep='\n')

ar=arr[1:2,0:3]
print('ar:',ar)
print('type(ar)',type(ar))
print('ar.ndim: ',ar.ndim)

ar=arr[-2:-1,1:3]
print('ar:',ar)

ar=arr[-2:-1,]
print('ar:',ar)

ar=arr[1:3]
print('ar:',ar)

ar=arr[0:3,0:2:2]
print('ar:',ar)

array=np.array([ [1,5,6,8],[1,-5,6,9],[8,58,16,88]])

for x in np.nditer(array):
    print(x,end=' ')

print('\n')

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)