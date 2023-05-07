import pandas as pd
# Define a dictionary containing information of employees
info = {'name': ['Parker', 'Smith', 'William', 'Robert'],
              'age': [38, 47, 44, 34],
               'language': ['Java', 'Python', 'JavaScript', 'Python']}
# Convert dictionary into DataFrame
info_pd = pd.DataFrame(info)
# Before renaming columns
print(info_pd)
info_pd.rename(columns = {'name':'Name','age':'AGE'}, inplace = True)
# After renaming columns
print("\nAfter modifying first column:\n", info_pd.columns)

print(info_pd)

info_pd.rename(index={0:'zero'},inplace=True)#implace allow to update the df
print(info_pd)
print(info_pd.index)

