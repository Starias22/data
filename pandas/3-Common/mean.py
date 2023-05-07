import pandas as pd

data=[1,20,33,45,12,48,-20,6,-4,7,2,0,8]
data=pd.Series(data)

print('data:',data,sep='\n')
mean=data.mean()
print('mean:',mean)

marks = pd.DataFrame({
                    'math':[15, 20, 32, 18 ,17],
                    'english': [2,5,6,9,7],
                    'french': [2,5,6,9,7]})

mean=marks.mean(axis=None)
print('mean:',mean)
desc=marks.describe()
print(desc)
print(desc.loc['mean'])
print(sum(desc.loc['mean'])/3)

means=marks.mean()
print('means:',means,sep='\n')

means=marks.mean(axis=0)
print('means:',means,sep='\n')

means=marks.mean(axis=1)
print('means:',means,sep='\n')
print(marks)


