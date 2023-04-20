import numpy as np
import pandas as pd

# Series
data=np.array(['P','a','n','d','a','s'])
series=pd.Series(data)

print(series)

print('type:',type(series))

#Data frames

data=['Python','Pandas','Tutorial']
dFrame=pd.DataFrame(data)
print(dFrame)