import pandas as pd

info = pd.Series(['C', 'C++', 'Python', 'Java','PHP'])
print(info.head())
print('',info.head(1),sep='\n')
print('',info.head(n=2),sep='\n')
print('',info.head(n=0),sep='\n')

marks=pd.DataFrame({'english':[15,12,14,8],'math':[18,15,9,9],
                    'chemistry':[12,8,18,19],'french':[17,7,12,13]})

print(marks)

print(marks.head(2))
