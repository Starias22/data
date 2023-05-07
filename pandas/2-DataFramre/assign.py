import pandas as pd
# Create an empty dataframe
info = pd.DataFrame()

# Create a column
info['ID'] = [101, 102, 103]

# View the dataframe
print(info)
# Assign a new column to dataframe
new=info.assign(PersonName = ['Smith', 'Parker', 'John'],age=15)
print(info)
print(new)
