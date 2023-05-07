from scipy.stats import poisson
import numpy as np

print('Gamma distribution a=2')
print('mean:',poisson.mean(mu=-1))
print('variance:',poisson.var(mu=-1))
print('standard deviation:',poisson.std(mu=-1))

#using numpy
arr=np.random.poisson(size=100)

print('Mean of the distribution:',np.mean(arr))
print('Std of the distribution:',np.std(arr))


#using scipy
arr=poisson.rvs(mu=2,size=100)# random variations


print('Mean of the distribution:',np.mean(arr))
print('Std of the distribution:',np.std(arr))

arr=poisson.rvs(mu=5,size=50)

print('Mean of the distribution:',np.mean(arr))
print('Std of the distribution:',np.std(arr))


