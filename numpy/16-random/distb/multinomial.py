import numpy.random as rd

x=rd.multinomial(n=6,pvals=[1/6 for i in range(6) ])

print(x)

x=rd.multinomial(n=6,pvals=[1/6 for i in range(6) ],size=10)

print(x)

