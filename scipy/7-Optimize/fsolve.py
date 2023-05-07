from scipy.optimize import fsolve

def f(x):
    return x**2+x-2

g=lambda x:x**2+5

def h(x):
    return ((x[0] + x[1])**2, 0)


res=fsolve(h,x0=[1,2])
print(res)

res=fsolve(h,x0=[4,-8.55])
print(res)

res=fsolve(f,x0=45)
print(res)

res=fsolve(g,x0=-5)
print(res)

