import csv

with open('write.csv','w') as output:
    #first row to write to the csv file
    firstrow=['name','age','tail','is good']

    csvwriter=csv.writer(output)
    #write a sinle row: a list
    csvwriter.writerow(firstrow)
    #data will be used as list of list of string(conversin)
    data=[
        ['Ezéchiel',20,1.78,True],
        ['Kevin',19,1.45,False],
        #only the first row is provided for that entry
        ['Jacob'],
        #empty row
        [],
        ['Jonas',45,1.80,False]

    ]
    #write several rows:list of lists
    csvwriter.writerows(data)
    row=('Mathias',55,1.88,False)
    csvwriter.writerow(row)
    lastrow=['Jeremie',66,1.85,True]
    csvwriter.writerow(lastrow)
    print('Writing finished')
    #pass