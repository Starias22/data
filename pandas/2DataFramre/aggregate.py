import pandas as pd
import numpy as np
info=pd.DataFrame([[-1,-5,-7],[10,-12,15],[18,21,24],[np.nan,np.nan,np.nan]],columns=['X','Y','Z'])


mn=info.agg('min')
print(mn)

absl=info.agg(func='abs')
print(absl)

x=info.agg(func=['sum','max','product'])

print(x)

x=info.agg({'x' : ['sum', 'min'], 'y' : ['min', 'max']})

print(x)