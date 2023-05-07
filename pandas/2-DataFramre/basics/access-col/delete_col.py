import pandas as pd
import numpy as np

print('************************')

df=pd.DataFrame(np.array([[20,22,25,14],[15,-20,-14,12],[14,12,14,18]]))
print('df before del 3',df,sep='\n')


del df[3]
print('df before del 3',df,sep='\n')


print('************************')

info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
   'three':[1,2,9,7,8,7]}

df=pd.DataFrame(info)

print('df before del three',df,sep='\n')
del df['three']
print('df after del',df,sep='\n')


val=df.pop('two')

print('df after pop two',df,sep='\n')

print('removed col after pop two',val)


print('************************')
ing=pd.DataFrame({'Name':['onion','garlic','tomato','pepper','chilli'],
                  'Unit price':[100,25,200,25,100],
                  'Quantity':[2,4,1,2,1]},
               index=np.arange(start=1,stop=6))

print('ing after pop Name',ing,sep='\n')



#delete the Name col
x=ing.pop('Name')
print('deleted col:',x)

print('ing after pop Name',ing,sep='\n')


