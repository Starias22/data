import pandas as pd
# Define a dictionary containing information of employees
info = {'name': ['Parker', 'Smith', 'William', 'Robert'],
              'age': [38, 47, 44, 34],
               'language': ['Java', 'Python', 'JavaScript', 'Python']}

info=pd.DataFrame(info)
print(info.columns)
print(info.index)