import numpy as np
#np.clip(x, min, max, out optional)
# all values <min are replaced by min
# all values >max are replaced by max
#out contains the result of the clip
x= np.arange(12)
y=np.clip(x, 3, 10)
print('x:',x)
print('y:',y)
w=np.zeros((12,),dtype=int)
print('w:',w)
z=np.clip(x,3,10,out=w)

print('z:',z)
print('w:',w)
