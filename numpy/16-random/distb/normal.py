from numpy import random as rd

x=rd.normal()
print(x)

x=rd.normal(size=15)
print(x)


x=rd.normal(size=(5,3))
print(x)

x=rd.normal(loc=0,scale=1,size=20)#centered, reduced dist
print(x)

