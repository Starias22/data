from scipy.optimize import minimize

def f(x):
    return x**2 + x + 2

g=lambda x:x**2+5
h=lambda x:x[0]**4+x[1]**2-5

res = minimize(f, 0)

print(res)
print(res.x)
mn=res.x[0]
print(mn)
print(f(mn))
print(f(-.5))

res = minimize(f, 0,method='COBYLA')
print(res.success)
print(res.x[0])

res=minimize(g,0)
mn=res.x[0]
print(mn)
print(g(mn))

res=minimize(h,x0=[1,2],method='Nelder-Mead')
mn=res.x
print(mn)
print(h(mn))