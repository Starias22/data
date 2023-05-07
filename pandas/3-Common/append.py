import pandas as pd

names=pd.Series(['Jacob','Roland','Gildas','Jérémie'])

print('names:',names,sep='\n')

others=pd.Series(['Roland','Isaac','Issa'])
names=names._append(others)
print('names:',names,sep='\n')

#ingore indexes: indexes are ignored and np.arange(start=0,stop=n) is used

third=pd.Series({'one':'Mathias','two':'Pogba','three':'Ulrich'})
names=names._append(others,ignore_index=True)
print('names:',names,sep='\n')


fruits=pd.DataFrame(data=('orange','mango','pineapple'))
print('Example of fruits:',fruits,sep='\n')

df=pd.DataFrame(['apple','lemon','mango'],index=[3,4,5])
fr=fruits._append(other=df)
print('Example of fruits:',fr,sep='\n')


df=pd.DataFrame(['banana','grapes'])
fr=fr._append(df,ignore_index=True)
print('Example of fruits:',fr,sep='\n')



info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
   'three':pd.Series([20,40,60],index=['a','b','c'])}

df=pd.DataFrame(info)

print(df)


ing=pd.DataFrame({'Name':['onion','garlic','tomato','pepper','chilli'],
                  'Unit price':[100,25,200,25,100],
                  'Quantity':[2,4,1,2,1]},
               index=np.arange(start=1,stop=6))



two=pd.DataFrame({'Name':['rice','beans'],'Quantity':[1,0.5]},index=[6,7])
ing=ing._append(two)



df=pd.DataFrame([['Cube',2,25],['salt',1]],columns=['Name','Quantity','Unit price'],index=(8,9))

ing=ing._append(df,ignore_index=True)

print(ing)




