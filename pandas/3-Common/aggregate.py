import pandas as pd
import numpy as np

data=pd.Series([20,25,66,-20,33])
mn=data.agg(min)


print('The min:',mn,sep='\n')

print('Plus 1:',data.agg(func=lambda x:x+1),sep='\n')
print('abs:',data.agg('abs'),sep='\n')


x=data.agg(['max','min','sum','prod','median','mean','var','std'])
print('\n\n:',x,sep='\n')
print(x['max'])


info=pd.DataFrame([[-1,-5,-7],[10,-12,15],[18,21,24],[np.inf,np.nan,np.nan]],columns=['X','Y','Z'])


mn=info.agg('min')
print(mn)

absl=info.agg(func='abs')
print(absl)

x=info.agg(func=['sum','max','product'])

print(x)

x=info.agg({'X' : ['sum', 'min'], 'Y' : ['min', 'max']})

print(x)