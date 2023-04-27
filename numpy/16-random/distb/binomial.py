import numpy.random as rd


x=rd.binomial(n=8,p=0.5)

"""
n: numer of trials: n>=0
p:probability of success : p in[0-1]
return the number of success:in[0-n]
"""


print(x)

x=rd.binomial(n=1,p=0.5)

print(x)


x=rd.binomial(n=8,p=0.33,size=10)
"""
size specifies the rep

return an array that containsthe numbers of success for each of the n trials
"""


print(x)