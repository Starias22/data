# csv

## Overview

CSV means Coma Seperated Values. It's a file extension of which content consists of simple data entries; each entry has fields that are seperated by coma(,); hense the name Coma Seperated Values(csv).

Note that these values are both considered as strings

Above we have an exemple of csv file content

Name,Age,Gender,Occupation
John,30,Male,Engineer
Sarah,25,Female,Teacher
David,42,Male,Accountant
Emily,28,Female,Doctor

Let's name that file person.csv for the future.

Name,Age,Gender,Occupation is the first entry of the file. It's consist of the fields names such as the name of th person, him age, gender and occupation

The other entries are the values of these fields.

Python provides a module called csv to manipulate csv files, meaning to read csv files and write into csv files.

To import the python csv module:

````python
import csv
````

## csv File reading

### open() in reading mode

First of all open the person.csv file using the ````open```` method.

````python
with open('person.csv','r') as file:
    #the rest of your code
````

'person.csv' represents the file name
'r' stands for reading; it's the file open mode
file is the file object and wil be used to manipulate our file.

By using the with keyword the file is automatically closed before the programm.

### cvs.reader()

The csv.reader() function is used to read a csv file. It takes as parameter the csv file object and retrns a csv object that allows to read the csv file. That object is an iterator and thencan be iterated over.

````python
#open a csv file
with open('read.csv','r') as file:
    #an iterable object
    csvreader=csv.reader(file)
    print(csvreader)#ancsv object
    ````
````

### next()

The next function is a python built-in object that returns the next item of an iterator. In our case, it is used to move from the current line or row or entry of the csv file, to the next one. It takes as parameter the csv reader object and returns the item following the current one. That item is a list of the fields

### line_num()

That method can be used to get the number of the current row of the csv file.

### seek()

We can use the seek method to set the position to read the csv file from. It takes as parameter an interger thatrepresents the number of characters. Then, seek(0) position the file object to the beginning of the file.

## Writing into csv file

### open() in writing mode

First of all open the write.csv file using the ````open```` method. The file is creted if not exist and recreated otherwise.

````python
with open('person.csv','r') as file:
    #the rest of your code
````

'write.csv' represents the file name
'w' stands for writing; it's the file open mode
file is the file object and wilb be used to write to our file.

By using the with keyword the file is automatically closed before the programm ends.

### cvs.writer()

The csv.writer() function is used to write to a csv file. It takes as parameter the csv file object and returns a csv object that allows to write to the csv file.

````python
#open a csv file
with open('read.csv','r') as file:
    #an iterable object
    csvwriter=csv.writer(file)
    print(csvwriter)#an csv object
    ````
````

### writerow()

The writerow() method is used to write a row to a csv file. It takes as parameter a list that represents the data entry to write into the file. The item of that list are the strings that represent the fields of the data.

### writerows()

The writerow() method is similar to the writerow method. It writes not only a row but several rows into a csv file. It takes as parameter a list or tuple that represents the data entries to write into the file. The item of that list are  lists of strings, each string representing a field of data.

## Summary

In summary, the csv module in Python provides a convenient way to manipulate csv files.
