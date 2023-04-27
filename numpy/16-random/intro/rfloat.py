import numpy.random as rd
import matplotlib.pyplot as plt
import seaborn as sbn

# Generate random float numbers between 0 and 1
x=rd.rand()

print('A random float in [0-1]',x)
print(type(x))

# Generate random float arrays, each item in [0-1]

##of shape(n,)
arr=rd.rand(20)
print(arr)
print(type(arr))

sbn.displot(arr)
plt.xlabel('Intervals')
plt.title('Random floats in [0-1]')
plt.show()

## of shape (n,m)
arr=rd.rand(2,3)
print(arr)



# Generate random float arrays, each item in [0-n]

arr=20*rd.rand(20)
print(arr)
sbn.displot(arr)
plt.xlabel('Intervals')
plt.title('Random floats in [0-20]')
plt.show()



arr=50*rd.rand(2,3)
print(arr)

#help(sbn.displot)

