import pandas as pd
import numpy as np

info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}

df=pd.DataFrame(info)

print(df)


df['three']=pd.Series([20,40,60],index=['a','b','c'])
print(df)

df['one']=[-20,5,6,20,4,7]
print(df)

df['two']='Ok'
print(df)

#update
df['three']=156
print(df)

df['three']+=5
print(df)





ing=pd.DataFrame({'Name':['onion','garlic','tomato','pepper','chilli'],
                  'Unit price':[100,25,200,25,100],
                  'Quantity':[2,4,1,2,1]},
               index=np.arange(start=1,stop=6))

print('ingredients:',ing,sep='\n')

ing['Quantity']*=3
print('ingredients:',ing,sep='\n')

ing['Quantity'][2]=10
print('ingredients:',ing,sep='\n')







