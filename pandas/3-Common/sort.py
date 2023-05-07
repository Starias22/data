import pandas as pd

marks={'english':15,'math':18,'chemistry':12,'french':17}
marks=pd.Series(marks)

print(marks.sort_index())


marks=pd.DataFrame({'english':[15,12,14,8],'math':[18,15,9,9],
                    'chemistry':[12,8,18,19],'french':[17,7,12,13]})

print(marks)
print(marks.sort_index(ascending=False))
print(marks.sort_index(axis=1))
print(marks.sort_values(by='french'))
print(marks.sort_index(ascending=False,axis='columns',inplace=True))#update the original df

print(marks.sort_values(by=['french','english'],kind='mergesort'))



