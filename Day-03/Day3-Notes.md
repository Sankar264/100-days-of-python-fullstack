
DataTypes
int =8
float

num_2=7.89
num=90.89
print(num//9)

strings:-string is sequence of character tht enclose in' '," ",""" """
string is imutable
so="python"
any=",.@9"
Concatination:-Here,the(+) operator act as to concatinate more than 2 strings
eg:-a="python"
b="language"
print(a+b)
indexing:-This is used access the particular character in the string by passing index position value
s="python is a language"
print(s[13])
index start from 0.........
we have negative indexing to count the position from last to first 
print([-3])
Methods:-
1. replace()
2. join()
3. split()
4. count()

replace:-
This method is used to replace/change any substring in that particular string 
Syntax:-varible_name.replace("old string","new string",count)
s="python is a language"
print(s.replace("python","java"))
s="python is a language"
print(s.replace("a","A",2))
join:-
This method used to add a new substring after each character in the string
Syntax:- "string".join(variable_name)
s="python is a language"
print("-".join(s))
split:-
This method can divide the string into different index into list,based on the string pass by us
syntax:-varible_name,split('substring')
s="python is a language"
print(s.split("is"))
count:-
used to count the substring and the particular string and also specify the index positions
syntax:-varible_name.count("substring",start index,ending index)
s="python is a language"
print(s.count("a",0,10)
String build-in functions
len()
max()
min()
len():-
This will find the length of the string which is number char present in that string
s="python is a language"
print(len(s))
max():-
will get the max character in the string
s="python is a language"
print(max(s))
min():-
will get the min character in the string
s="python is a language"
print(min(s))




