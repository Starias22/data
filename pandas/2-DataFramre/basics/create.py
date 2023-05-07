import pandas as pd
import numpy as np

# Create data frame

#empty data frame
df=pd.DataFrame()
print('Our empty data frame:',df)

#using list
marks=pd.DataFrame([20,15,14,16,18,17])
print('Student marks:',marks,sep='\n')

#using tuple
fruits=pd.DataFrame(data=('Orange','mango','pineapple'))
print('Example of fruits:',fruits,sep='\n')


#using numpy.ndarray
## of dim1
df=pd.DataFrame(np.array([14,15,16,17]))
print('Data frame from np:',df, sep='\n')

##of dim2
df=pd.DataFrame(np.array([[20,22,25,14],[15,-20,-14,12],[14,12,14,18]]))
print(df)

#using dictionary where values are list,tuple or series

employees=pd.DataFrame({'Number':np.arange(start=5,stop=9),
                        'Name':['John','Peter','Jacob','Roland'],
                        'Department':('Direction','Supervision','Security','Cleaning')})
print(employees)

info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}

df=pd.DataFrame(data=info)

print(df)

mydf=pd.DataFrame(data=[['John',15,20,15],['Andrew',3,18,20],['Roland',12,13,19]],columns=['Name','English','Math','Chemistry'],index=[1,2,3])

print(mydf)
