import pandas as pd

data=pd.Series([20,25,66,-20,33])

print(data.dtype)

sdata=data.astype(dtype=float)
print(sdata.dtype)

a = {'col1': [1, 2], 'col2': [3, 4]}
info = pd.DataFrame(data=a)
print(info.dtypes)
# We convert it into 'int64' type.
print(info.astype(dtype='int64').dtypes)
print(info.astype({'col1': 'int64'}).dtypes)
x = pd.Series([1, 2], dtype='int64')
print(x.astype('category'))
cat_dtype = pd.api.types.CategoricalDtype(
categories=[2, 1], ordered=True)
print(x.astype(cat_dtype))
x1 = pd.Series([1,2])
x2 = x1.astype('int64', copy=False)
x2[0] = 10
print(x1)  # note that x1[0] has changed too