import csv
print('csv:',csv)
print('csv version:',csv.__version__)

#open a csv file
with open('person.csv','r') as file:
    #an iterable object
    csvreader=csv.reader(file)
    print(csvreader)#ancsv object
    # extracting field names through first row
    fields = next(csvreader)
    print('field names:',fields)
    print('type(fields):',type(fields))#a list
    #read the first data entry: the row following the filed titles
    firstrow=next(csvreader)
    print('first entry:',firstrow)
    #read the second data entry:
    firstrow=next(csvreader)
    print('second entry:',firstrow)
    csvreader=csv.reader(file)
    #browse  the rest of the data entries
    #each item is a row
    for elt in csvreader:
        print(elt)
    #next(csvreader)# stop iteration
    #position the file cursor to the beginning
    file.seek(0)
    #create a new csvreader
    csvreader=csv.reader(file)
    #append all the elements to a list
    data=[]
    for row in csvreader:
        data.append(row)
    #data is now a list of lists of strings
    print('The input file contains',len(data), 'data entries')
    print('There are:\n',data)

    #the position of the iterator
    print('Num of the current row',csvreader.line_num)
    #reposition the next item next item file cursor to the beginning
    file.seek(0)
    csvreader=csv.reader(file)
    #print the number of rows that
    # have been iterated:0 at the beginning
    print('Num of the current row',csvreader.line_num)
