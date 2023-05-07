import pandas as pd
import numpy as np

#to access df col, row indexes are neccessary used
info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
   'three':pd.Series([20,40,60],index=['a','b','c'])}

df=pd.DataFrame(info)

print(df)

print('******First column:',df['one'],sep='\n')

y=df['three']
print (y)
print('type(y):',type(y))

print(df['one']['b'])
print(df['one']['f'])
print(df['three'][0])
print(df['two'][-1])
print(df['one']['b']//8)




print("df['one']+2*df['two']-df['three']:",df['one']+2*df['two']-df['three'],sep='\n')

ing=pd.DataFrame({'Name':['onion','garlic','tomato','pepper','chilli'],
                  'Unit price':[100,25,200,25,100],
                  'Quantity':[2,4,1,2,1]},
               index=np.arange(start=1,stop=6))

print('ingredients:',ing,sep='\n')

print('Quantities of products bought:',ing['Quantity'],sep='\n')
x=ing['Quantity'][1]


print(x,ing['Name'][1]+'(s)','have been bought')
x=ing['Quantity']

print(x)
print(x[2],x[1])








