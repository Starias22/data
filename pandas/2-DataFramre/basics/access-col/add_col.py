import pandas as pd
import numpy as np

#to cacess df col, row indexes are neccessary used
info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}

df=pd.DataFrame(info)

print(df)

y=df['three']=pd.Series([20,40,60],index=['a','b','c'])+10
print (y)
print(type(y))


df['four:sum(one,two,three)']=df['one']+df['two']+df['three']
print(df)


ing=pd.DataFrame({'Name':['onion','garlic','tomato','pepper','chilli'],
                  'Unit price':[100,25,200,25,100],
                  'Quantity':[2,4,1,2,1]},
               index=np.arange(start=1,stop=6))

print('ingredients:',ing,sep='\n')

ing['Def price']=ing['Unit price']*ing['Quantity']
print('ingredients:',ing,sep='\n')

print('Sum of depenses:',sum(ing['Def price']))




