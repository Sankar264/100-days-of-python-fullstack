'''
Type conversions
this is the process of converting one datatype to another datatype.....
Int:-string,float
eg:-
num=89
num_2 =float(num)
print(num_2)
print(type(num))
so=str(num)
print(type(so))
built-in functions:-
str()
float()
int()
list()
dict()
Float : string/integer
eg:-
num=8.9
how=str(num)
print(how)
print(type(how))
num_2=int(num)
print(num_2)
hai="90"
num=int(hai)
print(num+10)
hello="90.45"
num=float(hello)
print(num+20)
'''
any="python"#string to list
con=list(any)
print(con)
con_2=tuple(con)#list to tuple
print(con_2)
var=['p','y','t','h','o','n']
text="".join(var)
print(text)
var=['p','y','t','h','o','n']
some=tuple(var)
print(some)
python=[('a',1),('b',7)]
con=dict(python)
print(con)

fam=(1,2,3,4)
print(list(fam))
fam=('h','e','l','l','o')#tuple to string
text="".join(fam)
print(text)
