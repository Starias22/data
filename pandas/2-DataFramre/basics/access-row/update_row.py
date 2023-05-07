import pandas as pd
import numpy as np



ing=pd.DataFrame({'Name':['onion','garlic','tomato','pepper','chilli'],
                  'Unit price':[100,25,200,25,100],
                  'Quantity':[2,4,1,2,1]},
               index=np.arange(start=1,stop=6))

print('ingredients before update:',ing,sep='\n')


ing.loc[4]=pd.Series({'Name':'new product','Unit price':500,'Quantity':20})
print('ing.loc[4]:',ing.loc[4])
print('After update',ing,sep='\n')

ing.loc[1]=pd.Series({'Quantity':200,'Name':'product','Quantity':20})
print('After update',ing,sep='\n')





ing.loc[1:4]='*****'

print(ing)

marks=pd.DataFrame({'Test1':[18,20,18,13],'Test2':[15,12,13,14],'Test3':[5,5,16,15]},
                  index=['math','english','french','chemistry'])
print('marks:',marks,sep='\n')


marks[1:5:2]='/////'
print('marks:',marks,sep='\n')















