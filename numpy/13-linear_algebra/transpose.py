import numpy as np

arr=np.arange(start=1,stop=13)
print('arr:',arr,sep='\n')
arr=arr.reshape(3,4)
print('arr:',arr,sep='\n')

trp=arr.transpose()

print('trp:',trp,sep='\n')

trp=arr.transpose((0,1))

print('trp:',trp,sep='\n')

trp=arr.transpose((0,1))

print('trp:',trp,sep='\n')
