import numpy.random as rd

from matplotlib import pyplot as plt
import seaborn as sbn

# Generate random integer

## between 0 and n
x=rd.randint(10)
print(x)
print(type(x))

## in [x-y]
arr=rd.randint(20,30)
print(arr)
print(type(arr))

# Generate random intergers arrays


#each item in [0-y]
arr=rd.randint(100,size=(4,3))
print(arr)


#each item in [x-y];shape:(n,m)
arr=rd.randint(20,30,size=(4,3))
print(arr)

#shape n
arr=rd.randint(10,500,size=100)
print(arr)
sbn.displot(arr)
plt.title('100 Random ints in [10-500]')
plt.xlabel('Numbers')
plt.show()
