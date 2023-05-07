from scipy.stats import norm
import numpy as np

print('Features of the standard normal distribution')
print('mean:',norm.mean())
print('variance:',norm.var())
print('standard deviation:',norm.std())

#using numpy
arr=np.random.normal(loc=5,scale=2,size=100)

print('Mean of the distribution:',np.mean(arr))
print('Std of the distribution:',np.std(arr))


#using scipy
arr=norm.rvs(loc=5,scale=2,size=100)# random variations


print('Mean of the distribution:',np.mean(arr))
print('Std of the distribution:',np.std(arr))

arr=norm.rvs(size=50)# standard normal distribution

print('Mean of the distribution:',np.mean(arr))
print('Std of the distribution:',np.std(arr))


