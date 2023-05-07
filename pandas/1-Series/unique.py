import pandas as pd

colors=['green','yellow','blue','green','yellow','red','yellow','green','pinkle']
print(pd.unique(colors))
colors=pd.Series(colors,name='Colors')
print(colors)
unq=pd.unique(colors)#ndarray
print('Colors without repetition:',unq)
print(type(unq))
unq=pd.Series(unq,name='Unique colors')
print(unq)
