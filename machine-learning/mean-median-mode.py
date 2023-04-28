speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
import numpy as np

mean=np.mean(speed)
median=np.median(speed)

from statistics import mode
mode=mode(speed)

print('The arithmetic mean of speeds:',mean)
print('The median speed:',median)
print('The mode of speeds:',mode)
