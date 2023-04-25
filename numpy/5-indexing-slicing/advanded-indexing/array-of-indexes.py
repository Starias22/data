import numpy as np

# Indexing with array of indexes

arr=np.array([[1,2,2,3],[1,4,3,5],[0,-9,7,-25]])
ind=[0,1,1,2,2,1,0]# R1 R2 R2 R3 R3 R2 R1(7 rows)

print('arr:',arr,sep='\n')
print('ind:',ind,sep='\n')

print(arr[ind])