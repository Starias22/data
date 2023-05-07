from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import numpy as np

flabel='f(x)=x²+x-2'
glabel='g(x)=x²+5'
hlabel='h(x)=x+cos(x)'
klabel='h(x)=(x-8)**4'



bf='Before'
af='After'

def f(x):
    return x**2+x-2

g=lambda x:x**2+5
h=lambda x:x+np.cos(x)
k=lambda x:(x-8)**4

def findroot(f,a,b):
    print(f(a)*f(b))
    #aand b must be such that f(a)*f(b)<=0
    res=root_scalar(f,bracket=[a,b])
    print(res)
    if res.converged:
        r=res.root
        print('Zero between',a,'and',b,':',r)
        return r



def drawfunc(f,label,title,px=None):
    x=np.linspace(-10,20,100,endpoint=True)
    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Move both axes to pass through (0,0)
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))

    # Set the tick direction
    ax.yaxis.tick_left()
    ax.xaxis.tick_bottom()
    if px is not None:
        plt.scatter(px,f(px),marker='o',color='r',label='Zero(s) of f')

    plt.title(title)
    plt.plot(x,f(x),label=label)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()


drawfunc(f,flabel,bf)
x1=findroot(f,-4,0)
x2=findroot(f,0,2)
drawfunc(f,flabel,af,np.array([x1,x2]))

drawfunc(g,glabel,bf)
#x1=findroot(g,-4,4)

drawfunc(h,hlabel,bf)
x=findroot(h,-2,0)
drawfunc(h,flabel,af,np.array(x))

drawfunc(k,klabel,bf)
x=findroot(k,2.5,8)
drawfunc(k,klabel,af,np.array(x))
