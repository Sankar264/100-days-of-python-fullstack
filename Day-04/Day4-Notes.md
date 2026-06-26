
List datatype
list is a collection of different datatypes that are enclosed in [ ]
list is muttable
all_type = [1,'python',[1,2]]
immutable example
s="python is a languge"
print(s.replace('python','java'))#string is immutable
print(s)
muttable example
s=[1,2,3,4]
print(s)
s.append(6)
print(s)
_________________________________________________________________________________________________________________________________________________________________________________________
muttable                                           immutable
The data type can be modified                   The data type cannot be modify
example:-                                       example:-s="python is a languge"
s=[1,2,3,4]                                     print(s.replace('python','java'))#string is immutableprint(s)
s.append(6)                                     print(s)
print(s)
append():-
this is used to add new item into list, but it will add in the last index position
s=[1,2,3,4]
print(s)
s.append(6)
print(s)
extend():-
This is also add a item in the last index position but it will give each value
it will take only iterable eg:-list tuple
s=[1,2,3,4]
s.extend([30,90])
print(s)
s=[1,2,3,4]
s.extend('python')
print(len(s))

s= [1,2,'python is a language',[45,78,"java is a language",[1,23],90],'hello']
print(s)
print(s[3][3][1])
pop():-
used to del the value from the list , but it will del based on index position
syntax:- variablename.pop(index position)
s=[1,2,3,4,5]
s.pop(2)
print(s)
remove:-
used to delete the item from the list, but it will del direct value from the list
syntax:- variablename.remove(value)
s=[1,2,3,4,5]
s.remove(2)
print(s)
tuple:-
tuple is a collection of different datatypes represent in () and seperted by ,
it is immutble
how=(1,2,3,4,"python",[4,5],(90,78))
print(len(how))
print(how[4])
tuple methods
index()
count()
s=[90,89,55,23]
s.sort()
print(s)



