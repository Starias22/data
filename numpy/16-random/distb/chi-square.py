#Chi Square distribution

import numpy.random as rd

x=rd.chisquare(df=2)#degree of freedom

print(x)

x=rd.chisquare(2)#df

print(x)

x=rd.chisquare(20,size=(4,3))

print(x)