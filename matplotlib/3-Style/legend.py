import matplotlib.pyplot as plt
import numpy as np
"""xcoords=[1,5,9,6]
ycoords=[0,5,2,3]
plt.plot(xcoords,ycoords)
plt.show()"""

x=np.linspace(1,10,num=100)
y=np.sin(x)


plt.plot(x,y,label='f(x)=sin(x)')
plt.legend(loc='best')#the default

plt.show()

x=np.linspace(1,10,num=100)
y=np.log(x)


plt.plot(x,y,label='f(x)=ln(x)')
plt.legend()

plt.show()

x1=np.linspace(0,np.pi,num=100)
y1=-2+np.cos(x)

x2=np.linspace(0,np.pi,num=100)
y2=-2+np.sin(x)

plt.plot(x1,y1,label='f(x)=-2+cos(x)')
plt.plot(x2,y2,label='f(x)=-2+sin(x)')


plt.legend()

plt.show()


