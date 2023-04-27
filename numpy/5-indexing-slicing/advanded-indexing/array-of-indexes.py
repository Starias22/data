import numpy as np

# Indexing with array of indexes

arr=np.array([[1,2,2,3],[1,4,3,5],[0,-9,7,-25],[0,-9,98,88]])

ind=[1,0]#R2,R1
print('arr[ind]:',arr[ind],sep='\n')

ind=np.array([0,-1])#R1 Last-row
print('arr[ind]:',arr[ind],sep='\n')

ind=[0,-1]#R1 Last-row
print('arr[ind]:',arr[ind],sep='\n')


ind=[0,1,1,2,2,1,0]# R1 R2 R2 R3 R3 R2 R1(7 rows)

print('arr:',arr,sep='\n')
print('ind:',ind,sep='\n')

print(arr[ind])

ind=[[2,0]]
print(arr[ind])

ind=[[2,0],[1,2]]
print('arr[ind]:',arr[ind],sep='\n')


indf=np.array([[2,0],[1,2]])

print('arr[indf]:',arr[indf],sep='\n')

if np.array_equal(arr[ind],arr[indf]):
    print('Of course')




