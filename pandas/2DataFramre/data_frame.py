import pandas as pd
import numpy as np

df=pd.DataFrame()
print('Our data frame:',df)

marks=pd.DataFrame([20,15,14,16,18,17])
print('Student marks:',marks,sep='\n')

fruits=pd.DataFrame(data=('Orange','mango','pineapple'))
print('Example of fruits:',fruits,sep='\n')


df=pd.DataFrame(np.array([14,15,16,17]))
print('Dta fram from np:',df, sep='\n')

df=pd.DataFrame(np.array([[20,22,25,14],[15,-20,-14,12],[14,12,14,18]]))
print(df)

employees=pd.DataFrame({'Number':np.arange(start=5,stop=9),
                        'Name':['John','Peter','Jacob','Roland'],
                        'Department':('Direction','Supervision','Security','Cleaning')})
print(employees)

info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}

df=pd.DataFrame(info)

print(df)

print('******First column:',df['one'],sep='\n')
y=df['three']=pd.Series([20,40,60],index=['a','b','c'])
print (y)
print(type(y))

df['four:sum(one,two,three)']=df['one']+df['two']+df['three']
print(df)

del df['three']

print(df)

val=df.pop('two')

print(df)
print('removed col',val)

ing=pd.DataFrame({'Name':['onion','garlic','tomato','pepper','chilli'],
                  'Unit price':[100,25,200,25,100],
                  'Quantity':[2,4,1,2,1]},
                 index=np.arange(start=1,stop=6))

print('ingredients:',ing,sep='\n')

print('Quantities of bought products:',ing['Quantity'],sep='\n')
x=ing['Quantity'][1]
print(x,ing['Name'][1],'have been bought')
x=ing['Quantity']
print('Total number of products:',sum(x))

#Ad a colmn for price of each prod price*quantity


ing['Total']=ing['Unit price']*ing['Quantity']

print(ing)

# Total expense

print('The total expanse is',sum(ing['Total']))

#delete the toal col
del ing['Total']

print(ing)

#row selection

x=ing.loc[5]
print(x)

print(type(x))

print(x['Name'],x['Unit price'],x['Quantity'])

x=ing.iloc[4]
print(x)
print(x['Name'],x['Unit price'],x['Quantity'])

x=ing.iloc[-1]
print(x)
print(x['Name'],x['Unit price'],x['Quantity'])

x=ing.iloc[-2]
print(x)
print(x['Name'],x['Unit price'],x['Quantity'])
x=ing.loc[1:4]
print(x)

x=ing[0:3]
print(x)

x=ing[1:-1]
print(x)

two=pd.DataFrame({'Name':['rice','beans'],'Quantity':[1,0.5]},index=[6,7])
ing=ing._append(two)

print(ing)

print(ing['Unit price'][4])

ing['Unit price'][7]=600

print(ing)

df=pd.DataFrame([['Cube',2,25],['salt',1]],columns=['Name','Quantity','Unit price'],index=(8,9))

ing=ing._append(df)

print(ing)

ing=ing.drop(4)#pepper row dropped

print(ing)


