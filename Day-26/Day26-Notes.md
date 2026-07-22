'''
#-----------------------Day-26----------------------
File Handling
-------------
File handler is an object that gives more options like creating,updating
two ways to open the file.....
1.)open()
syntax:--> do=open('file_name','mode')
           close()
do=open('file_name','mode')
close()
2.)with (keyword):-
-------------------
syntax:- with open ('file_name','mode') as do:



do= open('demo.txt','r')
print(do.read())
with open('demo.txt','r') as do:
    print(do.read())
Modes:-
-------
r --> used to read the file, incase if the file is not present it will raise error
w---> used to write the text
with open('demo.txt','r') as do:
    print(do.read())
 

with open('demo.txt','w') as do:
    print(do.write('we are using file handling'))

#a--> this is used to add the text at last position inside the file
with open('demo.txt','a') as do:
    print(do.write('\nwe are using file user'))
    
with open('demo.txt','x') as do:
    print(do.write('\nwe are using file user'))
write():-
---------
this function is used to add the text inside a file or update a file with new text..........

read():-
--------
used to read a file and this read() will red file chunk by chunk....
we can also specific the size
readlines():-
-------------
this readlines() function will read only one line at a time....
with open('demo.txt','r') as do:
    print(do.readlines())
readline():-
'''
this function will read whole file and give it in a list each line is one index in that list....
with open('demo.txt','r') as do:
    print(do.readline())

    



   
