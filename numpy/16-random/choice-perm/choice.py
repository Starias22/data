import numpy.random as rd

data=[1,2,6,9,10,20]
print('data:',data)


choosen=rd.choice(data)

print('Choosen:',choosen)

res=rd.choice(data,size=5)
print('Result:',res)

res=rd.choice(data,size=(3,4))
print('Result:',res,sep='\n')

# set occuurence probabilies array using the p def arg
res=rd.choice(data,size=5,p=[0.05,0.1,0.3,0.5,0,0.05])
print('Result:',res)
