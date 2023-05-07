import pandas as pd
import numpy as np
#Empty serie

serie=pd.Series()
print(serie)

# Non-empty serie
## list
fruits=['orange','pineapple','mango','bananas','apple']
print('fruits as list: ',fruits)
fs=pd.Series((fruits))
print(fs)

##Tuple
fruits=tuple((fruits))
print('fruits as tuple: ',fruits)
fs=pd.Series((fruits))
print(fs)

##Dictionary

marks={'english':15,'math':18,'chemistry':12,'french':17}
print('marks as dict:',marks)
ms=pd.Series(marks)
print(ms)


## (numpy) array

personSizes=np.array([1.55,1.48,1.33,1.77,1.85,1.33],dtype=float)
print(personSizes)
pss=pd.Series(personSizes)
print(pss)

## Scalar

sc=pd.Series(2)
print(sc)

### data, index,dtype,name,copy

data=pd.Series([1,2,3,4],index=[-1,-2,-3,-4])
print(data)

sc=pd.Series(20,np.arange(10))
print(sc)

data=pd.Series(fruits,index=['1st','2nd','3rd','4th','5th'],dtype=str)
print(data)

data=pd.Series(20,dtype=float,name='My data')
print(data)

##Access data

print(pss[1])

pss[2]='OKay'
print(pss[2])

#print(pss[-1])

print(fs[2])

print('ms:',ms,sep='\n')
print('ms[3]',ms[3])


print("ms['english']:",ms['english'])

print('ms[-1]:',ms[-1])
print('ms[-3]:',ms[-3])

print('ms[0]:',ms[0])
print(type(ms[0]))
print('/////',ms[1:5])
print('/////',type(ms[1:5]))# Serie
print('/////',type(ms[1:-2]))# Serie






x=pd.Series(data=[2,4,6,8])
print('\nDescription of x***\n')
print('index:',x.index)
print('values:',x.values)
print('dim:',x.ndim)
print('shape:',x.shape)
print('dtype:',x.dtype)
print('itemsize:',x.size)
print('empty?:',x.empty)
print('has NaN values?:',x.hasnans)
print('nbytes:',x.nbytes)

y=pd.Series(data=[11.2,18.6,22.5], index=['a','b','c'])
print('\nDescription of y***\n')
print('index:',y.index)
print('values:',y.values)
print('ndim:',y.ndim)
print('shape:',y.shape)
print('dtype:',y.dtype)
print('size:',y.size)
print('empty?:',y.empty)
print('has NaN values?:',y.hasnans)
print('nbytes:',y.nbytes)


print('ms:',ms,sep='\n')


print(4+ms['english'])
print(4*ms['math'])
print(4.5-ms['french'])
print(4./-ms['french'])
print(-ms['french']/ms[-1]+3)

print(45+ms)

print(45*ms)
print(45/ms)
print(89*ms//22)

print(ms+fs)
print(ms*fs)
print(ms*ms)



print('ms:',ms,sep='\n')
print(len(ms))
print(ms.size)

ms+=2
print('Arithmetic mean of the student:',sum(ms)/ms.size)

cs=pd.Series({'english':2,'math':6,'chemistry':5,'french':2})
print('Serie of subjects coefficients:',cs,sep='\n')

print('Weighted mark in each subject:',ms*cs,sep='\n')
print('Weighted mean of the student:',sum(ms*cs)/sum(cs))











