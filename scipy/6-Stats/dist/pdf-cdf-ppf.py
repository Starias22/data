from scipy import stats
import numpy as np
import math
#Probability density function pdf: f(x):function densité de probabilité
#Cumultative distribution function cdf: F(x)=P(x<=x): function de répartition
#Percent poin function ppf function: F-1(x)



#Gauss/Normal distribution

f=stats.norm.pdf(x=5,loc=2,scale=3)
print(f)
f=stats.norm.pdf(x=5,loc=0,scale=1)#standard normal dist:loc=0,scale=1
print(f)
f=stats.norm.pdf(x=5)#standard normal dist:loc=0,scale=1
print(f)
F=stats.norm.cdf(x=5,loc=3)#scale=1
print('cdf:',F)







f=lambda x,loc=0,scale=1:(1/(scale*math.sqrt(2*math.pi)))*math.exp(-0.5*math.pow((x-loc)/scale,2))

print(f(5,2,3))
print(f(5,0,1))
print(f(5))

#expnential distribution

f=stats.expon.pdf(x=5,loc=2,scale=3)
print(f)
f=stats.expon.pdf(x=5,loc=0,scale=1)#standard normal dist:loc=0,scale=1
print(f)
f=stats.expon.pdf(x=5)#standard normal dist:loc=0,scale=1
print(f)
F=stats.expon.cdf(x=5,loc=3)#scale=1
print('cdf:',F)
ppf=stats.expon.ppf(q=1,loc=3)#scale=1
print('ppf:',ppf)

ppf=stats.expon.ppf(q=.5,loc=3)#scale=1
print('ppf:',ppf)



f=lambda x,loc=0,scale=1:(1/(scale*math.sqrt(2*math.pi)))*math.exp(-0.5*math.pow((x-loc)/scale,2))

print(f(5,2,3))
print(f(5,0,1))
print(f(5))



#expnential distribution

f=stats.expon.pdf(x=5,loc=2,scale=3)
print(f)
f=stats.expon.pdf(x=5,loc=0,scale=1)#standard normal dist:loc=0,scale=1
print(f)
f=stats.expon.pdf(x=5)#standard normal dist:loc=0,scale=1
print(f)
F=stats.expon.cdf(x=5,loc=3)#scale=1
print('cdf:',F)




#uniform distribution

f=stats.uniform.pdf(x=5,loc=2,scale=3)
print(f)
f=stats.uniform.pdf(x=5,loc=0,scale=1)#standard dist:loc=0,scale=1
print(f)
f=stats.uniform.pdf(x=5)#standard dist:loc=0,scale=1
print(f)
F=stats.uniform.cdf(x=5,loc=3)#scale=1
print('cdf:',F)



