import numpy as np
#np.linspace(start,stop,num=50,endpoint=True,retstep=False)
#nd array of 50 items from 1 to 20 with 20 inside
arr=np.linspace(start=1,stop=20)
print(arr)

#nd array of 15 items from 1 to 20 with 20 inside
arr=np.linspace(1,stop=20,num=15)
print(arr)

#nd array of 5 items from 1 to 20 with 20 outside
arr=np.linspace(start=1,stop=20,num=5,endpoint=False)
print(arr)

#nd array of 5 integer items from 1 to 20 with 20 outside
arr=np.linspace(start=1,stop=20,num=5,endpoint=False, dtype=int)
print(arr)

#nd array of 80 items from 1 to 20 with 20 inside
arr=np.linspace(start=1,stop=20,num=80,endpoint=True)
print(arr)
print('arr.size:',arr.size)

x=arr=np.linspace(1,20,num=5,retstep=True)
print(x)
print('array:',x[0])
print('step:',x[1])