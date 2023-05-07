import pandas as pd,numpy as np

data=[1,20,33,45,12,48,-20,6,-4,7,2,0,8]
data=pd.Series(data)
print(data)

desc=data.describe()
print('\ndesc:',desc,sep='\n')
print('type(desc):',type(desc))

print('min:',desc['min'])
print('max:',desc['max'])
print('size:',desc['count'])
print('std:',desc['std'])
print('mean:',desc['mean'])
print(desc['25%'])
print("75% of the data are less than or equal to",desc['75%'])

desc=data.describe(percentiles=[0.25,0.33,0.20])
print('\ndesc:',desc,sep='\n')

a1 = pd.Series(['p', 'q', 'q', 'r'])
print(a1.describe())


info = pd.DataFrame({
                    'marks':[15, 20, 32, 18 ,17],
                    'observations': ['Ok','great','ok','well','ok'],
                    'bonus': [2,5,6,9,7]})
print(info.describe(include=[np.number]))
print(info.describe(exclude=[object]))
print(info.describe())
print(info.describe(include=[object]))








