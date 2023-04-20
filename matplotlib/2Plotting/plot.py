import matplotlib.pyplot as plt

x=[1,-5]
y=[2,2.5]
plt.plot(x,y)
plt.show()

x=(4,-8)
y=(12.25,4)
plt.plot(x,y)
plt.show()

x=(4.33,-8)
y=[1.25,4]
plt.plot(x,y)
plt.show()

import numpy as np

x=np.array((4,-8))
y=np.array([12.25,4])
plt.plot(x,y)
plt.show()


x=(4,-8)
y=(12.25,4)
plt.plot(x,y,'o')
plt.show()

#multiple plots
x=(4,-8,5,9,6,9,8)
y=(12.25,4,5,6,7,0,1)
plt.plot(x,y)
plt.show()

# default x
y=(12.25,4,4,5,9,7)
plt.plot(y,'o')
plt.show()