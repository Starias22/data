# importing pandas as pd
import pandas as pd
import numpy as np

# create dataframe
info = pd.DataFrame({'P': ['Smith', 'John', 'William', 'Parker'],
        'Q': ['Python', 'C', 'C++', 'Java'],
        'R': [19, 24, 22, 25]})
print(info)
table = pd.pivot_table(info, index =['P', 'Q'])
print(table)
print(type(table))