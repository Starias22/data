import pandas as pd

marks=pd.DataFrame({'english':[15,12,14,8],'math':[18,15,9,9],
                    'chemistry':[12,8,18,19],'french':[17,7,12,13]})

x=marks.sample()
print(marks)
print(x)

x=marks.sample(3)
print(x)

x=marks.sample(n=2)
print(x)