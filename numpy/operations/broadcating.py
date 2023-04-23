import numpy as np

a = np.array([1,2,3,4,5,6,7])
b = np.array([20,4,6,8,10,12,14])

print('a:',a)
print('b:',b)

c = a+b;
print('c:',c)

c=a*b

print('c:',c)
print(a/b)
print(b//a)

"""a = np.array([1,2,3,4,5,6,7])
b = np.array([2,4,6,8,10,12,14,19])
c = a*b;
print(c)"""

a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
b = np.array([2,4,6,8])
print("\nprinting array a..")
print(a)
print("\nprinting array b..")
print(b)
print("\nAdding arrays a and b ..")
c = a + b;
print(c)

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[10], [20]])
print(a+b)