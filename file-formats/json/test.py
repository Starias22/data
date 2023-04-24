import json
"""print(json)
print(json.__version__)

employeeSalaries={'Jonas':14569,'Roland':15000,'Chris':156697}
print('Salaries(dict):',employeeSalaries)
js=json.dumps(employeeSalaries)
print(js)
print('type(js):',type(js))
person={
    'name':'Ezéchiel',
    'age':20,
    'tail':14.5,
    'friends':['Amstrong','Hervé','Stanislas'],
    'other details':[1,58.8,True,[-6,-8],'okay',(1,2,3)],
}
print('person:',person)
jsp=json.dumps(person)
print(jsp)
print('type(jsp):',type(jsp))
"""

# list conversion to Array
js=json.dumps(['Welcome', "to", "GeeksforGeeks"])
print(js)
print('type:',type(js))

# tuple conversion to Array
js=json.dumps(("Welcome", "to", "GeeksforGeeks"))
print(js)
print('type:',type(js))

# string conversion to String
js=json.dumps("Hi")
print(js)
print('type:',type(js))

# int conversion to Number
js=json.dumps(123)
print(js)
print('type:',type(js))
# float conversion to Number
js=json.dumps(23.572)
print(js)
print('type:',type(js))

# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))

# None value to null
print(json.dumps(None))