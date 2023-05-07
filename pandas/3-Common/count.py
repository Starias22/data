import pandas as pd
import numpy as np
data=[1,20,33,45,12,48,-20,6,-4,7,2,0,8]
data=pd.Series(data)
print(data.count())

info = pd.DataFrame({"Person":["Parker", "Smith", "William", "John"],
"Age": [27., np.inf, np.nan, 32]})
print(info.count())

print(info.count(axis='columns'))
print(info.count(axis='index'))