from scipy.optimize import root

def h(x):
    return ((x[0] + x[1])**2, 0)

def f(x):
    return x**2+x-2

g=lambda x:x**2+5

res=root(f,x0=2)
print(res)
print('root:',res.x)
print('success?',res.success)

res=root(g,x0=2)
print(res)
print('root:',res.x)
print('success?',res.success)

res=root(h,x0=[1,2])
print(res)
print('root:',res.x)
print('success?',res.success)

res=root(h,x0=[4,-5])
print(res)
print('root:',res.x)
print('success?',res.success)
print(h([5,-5]))
