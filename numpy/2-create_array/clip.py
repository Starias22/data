import numpy as np
x= np.arange(12)
y=np.clip(x, 3, 10)
print('x:',x)
print('y:',y)
w=np.zeros((12,),dtype=int)
z=np.clip(x,3,10,out=w)

print('z:',z)
print('w:',w)
