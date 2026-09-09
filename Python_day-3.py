'''
Python project --> POP/OOP --> DSA (Logic based --> pattern based --> platform
POP (Procedure Oriented Programming) --> Dividing the entire code into  blocks--> procedures --> functions (def)
Functions --> A reusable block of code (A block of statements which preforms a specific task)
Syntax:-

def <funcname>(parameters): #func defn
        """Doc String"""
        Statement(s)...
        ................ #body of func
        return value(s)...
fname(args) #func call
#example
def add(a,b):
    """Addition Function"""
    c=a+b
    return c
print(add(6,7))#addition
c,d ='codegnan','python'
print(add(c,d))#Concatination
a,b=map(str,input("enter name").split(','))
print(add(a,b))
print(add([1,3,4],[5,6,7])) #merging
#print(add(1,2,3,4)) #positional arguments fail
#Varible length arguments --> *args we can pass any number of positional arguments
#arguments --> data will be stored in tuple...

def sample(*a):#star args
    """Demo of varible length aruguments"""
    print(a)
    print(type(a))
sample(2,3,4,5)
sample('codegnan',[1,2,3,4],'poll',(2+1j))

marks=[1,2,3,4]
sample(marks)
sample(*marks)
#* is used to unpack the values into a collection 
a,*b,c=12,3,4,56,86,43,44
print(a)
print(b)
print(c)

def add(*a):
    print(a)
    result=0
    for i in a:
        if type(i) in [int,float,tuple]:
            result+=i
    return(result)
print(add(2,3,4,5,6))
print(add('sankar',22,22.33,(kumar)))
#keyword arguments --> we can pass the name for arguments
def batch(name,age,place):
#def batch(name="sankar",age=21,place='hyd'): ---> non default always follows
    """Keyword arguments usage"""
    print(f'{name} is in {place} and its {age}')
batch('codegnan',1,'vizag')
batch(place='hyd',name='ekanth',age=23)
#keyword arguments only needs name matching not order
batch(name="sankar",age=23)
#default arguments can accept a value as default
'''
print(4,5)
print(4,5,sep=':')#here keyword argument is sep and we are changing the default value for sep
#keyword varible length arguments (**kwargs)--> any number of keyword arguments,data is stored in dictionary
def batch(**a):
    """keyword varible length argument usage"""
    print(a)
    print(type(a))
batch()
batch(name="bharat",age=21,place="vizag",branch="cse")
data={'names':['Deepika','sree'],
      'place':[ 'vizag','rajahmendry']}
#batch(**data)
data.update({'batch':'PFS-VSP-004'})
batch(**data)



    
