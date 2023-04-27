import numpy.random as rd

x=rd.poisson()

print(x)

x=rd.poisson(lam=5)#default 2

print(x)

x=rd.poisson(lam=5,size=20)

print(x)

x=rd.poisson(lam=5,size=(5,15))

print(x)