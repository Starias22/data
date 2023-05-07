import pandas as pd

data=[1,20,20,45,12,48,-20,6,-4,7,6,0,8]
data=pd.Series(data)

x=data.drop_duplicates()
print(x)

emp = {"Name": ["Parker", "Smith", "William", "Parker"],
"Age": [21, 32, 29, 21]}
info = pd.DataFrame(emp)
print(info)

info=info.drop_duplicates()
print(info)

emp = {"Name": ["Parker", "Smith", "William", "Parker"],
"Age": [23, 32, 29, 21]}
emp = pd.DataFrame(emp)
print(info)

info=emp.drop_duplicates()
print(info)

emp = {"Name": ["Parker", "Smith", "William", "Parker"],
"Age": [23, 21, 21, 22],
'Gender':['F','M','M','F']}

emp = pd.DataFrame(emp)
print(info)

info=emp.drop_duplicates(subset='Name')
print(info)

info=emp.drop_duplicates(subset=['Gender','Age'])
print(info)

info=emp.drop_duplicates(subset=['Gender','Age'],keep='first')
print(info)


info=emp.drop_duplicates(keep='last')
print(info)

info=emp.drop_duplicates(keep=False)
print(info)

