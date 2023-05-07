from numpy.random import randint
from scipy.stats import describe

#generate 30 random int in [0-100]
arr=randint(0,101,30)
print(arr)

x=describe(arr)
print(x)
print(type(x))
print(x[0])

for item in x:
    print(item)