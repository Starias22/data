
import pandas as pd
import numpy as np

data=pd.Series([20,25,66,-20,33])
sqrt=data.apply(np.sqrt)


print('The squared root:',sqrt,sep='\n')

print('squared:',data.apply(lambda x:x**2),sep='\n')



info = pd.DataFrame([[14, -19,20,15],
                    [12,15,-10,13],
                    [9,-15,-5,17] ] , columns=['math', 'french','english','chemist'])
print('marks:',info,sep='\n')

def double(x):
    return 2*x

db=info.apply(double)

print('double mark:',db,sep='\n')

sq=info.apply(abs)

print('abs mark:',sq,sep='\n')

sm=info.apply(sum)
print('sum mark:',sm,sep='\n')

print('marks+1:',info.apply(lambda x:x+1),sep='\n')


prod=info.apply(np.product,axis=0)
print('marks prod axis 0:',prod,sep='\n')

prod=info.apply(np.product,axis='index')
print('marks prod axis index:',prod,sep='\n')

prod=info.apply(np.product,axis=1)
print('marks prod axis 1:',prod,sep='\n')

prod=info.apply(np.product,axis='columns')
print('marks prod axis col:',prod,sep='\n')


xx=info.apply(lambda x: x**2)
print('math squared:',xx,sep='\n')






