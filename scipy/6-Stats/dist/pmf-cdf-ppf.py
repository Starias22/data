from scipy import stats
import numpy as np
import math
#Probability mass function pmf: P(x=k): probabilité
#Cumultative distribution function: F(k)=P(x<=k): function de répartition


#Poisson

p=stats.poisson.pmf(k=1,mu=2)
print(p)
F=stats.poisson.cdf(k=1,mu=2)
print('cdf:',F)

P=lambda k,mu:math.pow(mu,k)*math.exp(-mu)/math.factorial(k)
print(P(1,2))

mu=5
dist=stats.poisson.rvs(mu,size=100)
print(dist)
print(type(dist))
pmfs=np.zeros(dist.max()+1)
print(pmfs)

for i in range(dist.min(),dist.max()+1):
    pmfs[i]=stats.poisson.pmf(i,mu=mu)

print(pmfs)
print(np.sum(pmfs))

#bernouli k in {0,1}

p=stats.bernoulli.pmf(k=0,p=0.2)
print(p)
p=stats.bernoulli.pmf(k=1,p=0.2)
F=stats.bernoulli.pmf(k=1,p=0.2)

print(p)

def P(k,p):
    if k==1:
        #success
        return p
    else:
        #failure
        return 1-p
print(P(1,0.3))
print(P(0,0.3))

print('cdf:',F)

ppf=stats.bernoulli.ppf(q=1,p=0.8)
print('ppf:',ppf)

ppf=stats.bernoulli.ppf(q=0,p=0.2)
print('ppf:',ppf)




