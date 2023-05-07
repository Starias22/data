import pandas as pd
import numpy as np
index = pd.Index(['orange','mango' ,'orange',
                'pineapple','apple','mango','orange'])
x=index.value_counts()# return a serie of unique values of index in desc order
# the numbers of occurences are the values of that serie
print(x)
print(type(x))

index=pd.Index([1,2,5,2,3,2,1,5,6,4])
x=index.value_counts(normalize=True)#divide each number of occ by the size of the serie
print(x)
x=index.value_counts(sort=False)#respect the order, do not sort(True by default)
print(x)

x=index.value_counts(bins=True)
print(x)

x=index.value_counts(dropna=False)# count NaN(dropna is default True)
print(x)

