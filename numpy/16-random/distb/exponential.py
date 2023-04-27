import numpy.random as rd

x=rd.exponential()

print('x:',x)

x=rd.exponential(scale=2)#default 1

print('x:',x)

arr=rd.exponential(scale=2,size=15)

print('arr:',arr,sep='\n')

arr=rd.exponential(scale=2,size=(3,4))

print('arr:',arr,sep='\n')

