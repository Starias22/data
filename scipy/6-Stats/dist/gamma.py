from scipy.stats import gamma
import numpy as np

print('Gamma distribution a=2')
print('mean:',gamma.mean(a=2))
print('variance:',gamma.var(a=2))
print('standard deviation:',gamma.std(a=2))

#using numpy
arr=np.random.gamma(2,scale=2,size=100)

print('Mean of the distribution:',np.mean(arr))
print('Std of the distribution:',np.std(arr))


#using scipy
arr=gamma.rvs(a=5,scale=2,size=100)# random variations


print('Mean of the distribution:',np.mean(arr))
print('Std of the distribution:',np.std(arr))

arr=gamma.rvs(a=2,size=50)#standard Guass distribution: scale=1

print('Mean of the distribution:',np.mean(arr))
print('Std of the distribution:',np.std(arr))


