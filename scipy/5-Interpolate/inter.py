from scipy import interpolate as intp
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 10)
y = np.cos(x**2/3+4)
plt.scatter(x,y,color='r')
plt.show()

fun1 = intp.interp1d(x, y,kind = 'linear')
fun2 = intp.interp1d(x, y,kind = 'cubic')
fun3 = intp.interp1d(x, y,kind = 'quadratic')
fun4 = intp.interp1d(x, y,kind = 'slinear')
fun5 = intp.interp1d(x, y,kind = 'zero')
fun6 = intp.interp1d(x, y,kind = 'nearest')






xnew = np.linspace(0, 4,30,endpoint=True)

plt.scatter(x,y)
plt.plot(xnew,fun1(xnew),'--',xnew,fun2(xnew),'--',
        xnew,fun3(xnew),'--',xnew,fun4(xnew),'--',
        xnew,fun5(xnew),'--',xnew,fun6(xnew),'--')
plt.legend(['Plots to interpolate',
            'Linear','Cubic','Quadratic',
            'S-linear','Zero','Nearest'])
plt.show()
