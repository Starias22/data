import numpy as np

csv_header=np.loadtxt('person.csv',delimiter=',',dtype='str')[0]

print('The heaader of the CSV file:',csv_header)
csv_data=np.loadtxt('person.csv',skiprows=1,delimiter=',',dtype='str')
print('csv data:',csv_data,sep='\n')


