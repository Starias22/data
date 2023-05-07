import pandas as pd
import numpy as np



ing=pd.DataFrame({'Name':['onion','garlic','tomato','pepper','chilli'],
                  'Unit price':[100,25,200,25,100],
                  'Quantity':[2,4,1,2,1]},
               index=np.arange(start=1,stop=6))

print('ingredients:',ing,sep='\n')

#loc
x=ing.loc[4]#item with 4 as row index
print(x)

print(type(x))# a serie

print('Indexes of x:',x.index)
print('Values of x:',x.values)


print('Name of the product x:',x['Name'])
print('Unit price of the product x:',x['Unit price'])
print('Quantity of the product x:',x['Quantity'])


print(x[0],x[1],x[-1])

x=ing.loc[1:4]#row index 1 and 4 inside
print('x:',x,sep='\n')
print('type(x):',type(x))#a data frame
y=ing.loc[1:]#from index one to the last
print('y:',y,sep='\n')


#iloc

## access a row by index:indexing ret serie
x=ing.iloc[4]# the 5th elm
print(x)
print(x['Name'],x['Unit price'],x['Quantity'])

x=ing.iloc[-1]# the last element
print(x)
print(x['Name'],x['Unit price'],x['Quantity'])

x=ing.iloc[-2]#penultimate element
print(x)
print(x['Name'],x['Unit price'],x['Quantity'])


## access a set of rows by indexes: slicing: ret data frame
x=ing.iloc[1:4]#index 4(5th elt) outside
print(x)

print('+++',x['Name'],sep='\n')

x=ing[0:3]#3(4th elt) outside
print('***',x)

x=ing[1:-1]#the last item outside
print(x)





info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=[ 'b', 'c', 'd', 'e', 'f','a']),
   'three':pd.Series([20,40,60],index=['a','b','c'])}

df=pd.DataFrame(info)

print(df)

print('index a:',df.loc['a'],sep='\n')# a serie
print('index f:',df.loc['f'],sep='\n')
print('from index a to d:',df.loc['a':'d'],sep='\n')
print('from index a to d in leaps of 2:',df.loc['a':'d':2],sep='\n')


print('First item:',df.iloc[0],sep='\n')# a serie
print('Last item:',df.iloc[-1],sep='\n')# a serie
print('5th item:',df.iloc[4],sep='\n')# a serie

print('All items:',df.iloc[0:],sep='\n')# a data frame
print('From 3rd item to 5th item:',df.iloc[2:5],sep='\n')# a data frame
print('From 3rd item to penultimate item:',df.iloc[2:-2],sep='\n')# a data frame
print('From 1st to 6th in leaps of two',df.iloc[0:6:2],sep='\n')



print('From 2nd item to 5th item:',df[1:5],sep='\n')# a data frame
print('From 2nd item to the item before the penultimate one:',df[1:-2],sep='\n')# a data frame
df[1:5:3]#from second to5th in leaps of 3
df['a':'f']
df['b':]

marks=pd.DataFrame({'Test1':[18,20,18,13],'Test2':[15,12,13,14],'Test3':[5,5,16,15]},
                  index=['math','english','french','chemistry'])
print('marks:',marks,sep='\n')

print(marks['english':'chemistry'],sep='\n')
print(marks.loc['english':'chemistry'],sep='\n')














