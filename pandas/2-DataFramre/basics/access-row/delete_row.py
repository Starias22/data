import pandas as pd
import numpy as np



info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}

df=pd.DataFrame(info)

x=df.drop('a')
print('x:',x,sep='\n')
print(type(x))

print(df)


