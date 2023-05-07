from scipy import integrate as intg
import numpy as np

def f(x):
    return 12*x

print(intg.quad(f,a=0,b=1))

g=lambda x:np.cos(x)
val,err=intg.quad(g,0,np.pi/2)
print('val:',val)
print('error:',err)


f = lambda x, y : 12*x
g = lambda x : 0
h = lambda y : 1
i = intg.dblquad(f, 0, 0.5, g, h)
print(i)
#tplquad()
#nquad()
