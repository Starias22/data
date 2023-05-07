import numpy as np
from scipy import io

#create a nd-array

arr=np.arange(0,12).reshape(4,3)
print('arr:',arr,sep='\n')

io.savemat('file',{'Array name':arr})

x=io.loadmat('file')
print(x)
print(x['Array name'])
mat=io.whosmat('file')
print(mat)