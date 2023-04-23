import numpy as np

def trace(array):
    if array.ndim!=2 or array.shape[0]!=array.shape[1]:
        return None
    trace=0
    for i in range(array.shape[0]):
        trace+=array[i,i]
    return trace
def magic(array):

    trace=trace(array)
    mat=np.fill(array.shape,trace)
    row_sum_mat=np.sum(axis=1)
    col_sum_mat=np.sum(axis=0)
    return mat==row_sum_mat==col_sum_mat


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
for elt in arr:
    print(elt)
    print("type(elt):",type(elt),"elt.ndim:",elt.ndim)

print(len(arr))
arr2=np.full((3,3),2)
print(arr2)

#Tests
trc=trace(arr)
print('trace(arr):',trc)
trc=arr2

trc=trace(arr2)
print('trace(arr2):',trc)

arr3=np.array([1,2,3])#an 1D array
trc=trace(arr3)
print('trace(arr3):',trc)

arr3=np.array([[1,2,3],[1,2,3]])#an 2D array but not a squared matrix
trc=trace(arr3)
print('trace(arr3):',trc)




