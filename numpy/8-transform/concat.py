import numpy as np

x=np.array([[1,2,3],[3,4,-20]])
y=np.array([[12,30,10]])
print('x:',x)
print('y:',y)
z=np.concatenate((x,y))

print('z:',z)

z=np.concatenate((x,y),axis=0)
print('z:',z)


#z=np.concatenate((x,y),axis=1)#error

x=[[1,2,3,9],[2,3,5,6],[1,0,-5,2]]
y=[[2,5,1],[2,0,-5],[-8,3,6]]

z=np.concatenate((x,y),axis=1)
print(z)

z=np.concatenate((x,y),axis=None)
print('z:',z)

x=np.ma.arange(3)
y=np.arange(3,6)

print('x:',x)
print('y:',y)
x[1]=np.ma.masked

print('x:',x)
print('y:',y)

print(x[1])
print(type(x[1]))
print(x[1].dtype)

z1=np.concatenate([x,y])
z2=np.ma.concatenate([x,y])

print('z1:',z1)
print('z2:',z2)

print(type(z2))

a= np.array([[1,2,30],[10,15,4]])
b = np.array([[1,2,3],[12, 19, 29]])

print('a:',a)
print('b:',b)
print("Arrays vertically concatenated\n",np.vstack((a,b)));
print("Arrays horizontally concatenated\n",np.hstack((a,b)))

print('***')
z=np.stack([a,b])
print(z)
print(type(z))
print(z.size)
print(z.shape)

a= np.array([[1,2,30],[10,15,4]])
b = np.array([[1,2,3],[12, 19, 29]])

print(np.concatenate([a,b,b,a]))
print(np.concatenate([a,b,b,a],axis=0))
print(np.concatenate((a,b,b,a),axis=1))
print(np.concatenate([a,b,b,a],axis=None))

print(np.vstack([a,b,b,a]))
print(np.hstack([a,b,b,a]))
print(np.stack([a,b,b,a]))