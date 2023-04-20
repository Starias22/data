import pandas as pd
import numpy as np
index = pd.Index(['orange','mango' ,'orange',
                'pineapple','apple','mango','orange'])
x=index.value_counts()# return e serie  unique values of index in desc order
# the nmber of occurences is the values off that serie
print(x)
print(type(x))

index=pd.Index([1,2,5,2,3,2,1,5,6,4])
x=index.value_counts(normalize=True)
print(x)
x=index.value_counts(sort=False)#respect the order, do not sort(True by default)
print(x)

x=index.value_counts(bins=True)
print(x)

x=index.value_counts(dropna=False)# count NaN(dropna is default True)
print(x)

print(np.std([4,2,1,6,3]))
print(np.std([6,9,15,2,-17,15,4]))