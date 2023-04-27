import numpy as np
arr=np.array([1,2,3,4,3,6,2,4,2,1])

a=np.unique(arr)

print('arr:',arr,sep='\n')
print('a:',a,sep='\n')

a=np.unique([1,2,3,4,3,6,2,4])
print('a:',a,sep='\n')

a=np.array([[1,2,2,3,9],[1,4,3,5,8]])

b=np.unique(a)
print('a:',a,sep='\n')
print('b:',b,sep='\n')



b=np.unique(a,axis=None)
print('a:',a,sep='\n')
print('b:',b,sep='\n')





a=np.array([2,6,9,7,0,7,9,5])
res,indexes=np.unique(a,return_index=True)


print('res:',res,sep='\n')
print('indexes:',indexes,sep='\n')

print(a[indexes])

if np.array_equal(res,a[indexes]):
    print('Alright')


a = np.array([[1, 1, 0], [1, 1, 0], [2, 3, 4],[5, 9, 8],[2, 3, 4]])
b=np.unique(a,axis=0)
print('a:',a,sep='\n')
print('**b:',b,sep='\n')


a = np.array([[1, 1, 0], [1, 1, 0], [2, 2, 4],[5, 5, 8],[2, 2, 4]])
b=np.unique(a,axis=1)
print('a:',a,sep='\n')
print('b:',b,sep='\n')

