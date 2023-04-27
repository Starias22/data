import numpy.random as rd

x=rd.uniform()# in [0-1]
print(x)

x=rd.uniform(2,5)
print(x)

x=rd.uniform(5,2)
print(x)

x=rd.uniform(10,100,size=20)
print(x)


x=rd.uniform(10,100,size=(5,4))
print(x)