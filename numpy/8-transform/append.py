import numpy as np
a=np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
b=np.array([[11, 21, 31], [42, 52, 62], [73, 83, 93]])

print('a:',a)
print('b:',b)
c=np.append(a,b)
print('c:',c)

c=np.append(a,b,axis=None)
print('c:',c)

c=np.append(a,b,axis=0)
print('c:',c)
c=np.append(a,b,axis=1)
print('c:',c)