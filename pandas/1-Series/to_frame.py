import pandas as pd

lastnames=pd.Series(['Chandler','Tiffany','Wilson','Chris','John'],name='last')
print(lastnames)

df=lastnames.to_frame()
print(df)

df=lastnames.to_frame(name='lastnames')
print(df)
print(type(df))