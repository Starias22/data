import numpy as np
a=45
print('a:',a)
b=a
print('b:',b)
a=1455
print('a:',a)
print('b:',b)

print(b==a)
print(b is a)
print(id(a),id(b))



b=-20
a=np.array([4,5,6,7,20])
print('a:',a)

b=a
print('b:',b)

b[0]=55
print('b:',b)
print('a:',a)#changes made to b affect a and vise versa: a and b share the same memory
a=np.array([45,20])
print('a:',a)
print('b:',a)

#check
print(b is a)
# they have the same id
print('id(a):',id(a))
print('id(b):',id(b))
print('id(a)==id(b)?',id(a)==id(b))

#share the same memory
print('Do a and b share the same memory?',np.shares_memory(a, b))
#b is said to be a view of a

b=a.copy()
print(a==b)
print(np.shares_memory(a, b))
print(a is b)

b[-1]=4566#changes made to b won't affect a and vise versa
print(a)
print(b)

#print(b==a)
b=np.array([4,-5,-6,3,0,7])
x=b.view()# x and b share memory
print(x)
print(b)
x[0]+=20
print(x)
print(b)
