import numpy as np
from scipy.stats import kstest
from scipy.stats import poisson


v = np.random.normal(size=100)

res = kstest(v, 'norm')

print(res)



