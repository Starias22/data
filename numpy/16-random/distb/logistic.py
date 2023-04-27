import numpy.random as rd
x=rd.logistic()
print(x)


x=rd.logistic(size=15)
print(x)

#loc: the mean-- default 0
x=rd.logistic(loc=15)
print(x)

#scale: default 1
x=rd.logistic(scale=145,loc=2,size=10)
print(x)