'''
OOP - Encapsulation, Inheritance, Polymorphism, Abstraction


#Abstraction - It is the process of hiding necessary details and display / access relevant  iinformation only
#Module abc

import abc
#print(dir(abc))  #It  returns available methods, classes.......

from abc import ABC, abstractmethod

#Now we will create some base classes to have abstraction applied for all classes
class Content(ABC):
    @abstractmethod
    def upload(self):
        print("******")
        #pass
class Photo(Content):
    """This dervied class will have upload features"""
    def upload(self):
        print("Photo is uploaded successfully")
        print("Photo is compressed and edited as per filters choosen")
        print("Photo is posted")
class Video(Content):
    """This is dervied class will have video upload features"""
    def upload(self):
        print("Encoding the video")
        print("Cmpressed and filters are added")
        print("Edited video is published successfully")
class Reel(Content):
    """This dervied class will have reel uploading features"""
    def upload(self):
        print("Timing and content is choosen")
        print("Reel content is mapped with time and audience")
        print("Reel is edited and uploaded successfully")
    
content_ = [Photo(), Video(), Reel()]
#print(content_)
for content in content_:
    content.upload()



#List Compprohensions - Optimized way of creating and using lists

Syntax - [expression for var in collection / function]




list_ = [1, 2, 3, 4]
for i in range(1, len(list_) +  1):
    l = i ** 2
    list_.append(l)
print(list_)

list_ = [1, 2, 3, 4]
for i in list_:
    l = i ** 2
    list_.append(l)
    print(list_)


#In above it gets into infinite and also limits be exceeded
lst = []
for i in range(10):
    lst.append(i)
    print(lst) #In this case it prints for every iteration
print(lst)



list_ = [i ** 3 for i in range(1, 20)]
print(list_)



#To access desired elements and make change

data = ["sankar","ekanth","Bharat","rohith"]
new_data = []
#Change every name to uppercase
for i in data:
    new_data.append(i.upper())
print(new_data)

#Using List compression
new_data = [i.title() for i in data]
print(new_data)

#To update each value in a list

marks = [14, 15, 12, 13]
d = [i + 30 for i in marks]
print(d)


#Every list comprehension can be converted to loops, but every loop cannot be converted to list comprehension..

#List Comprehension with if clause
#Syntax: [expression for var in collection/function if <condition>]

g = [i for i in range(1,21) if i%2==0]
print(g)
h = [i**2 for i in range(1,21) if i%2==0]
print(h)

#write this cases as functions
#even numbers
def even_number():
    h=[]
    for i in range(1,21):
        if i%2==0:
            h.append(i)
    return h
print(even_number())
#square
def square():
    sq=[]
    for i in range(1,21):
        if i%2==0:
            sq.append(i**2)
    return sq
print(square())
#Same above case using filter
h=list(filter(lambda i:i%2==0,range(1,21)))
print(h)

k=list(filter(lambda x: len(x)==6,['codegnan','python','data','sankar']))
print(k)
#in the below case length of each object is returned in a new list
h=list(map(lambda x:len(x),['codegnan','python','data','sankar']))
print(h)
#group of values --> map
j =list(map(int,input().split(',')))
print(j)
a,b,c,d =map(int,input().split())
print(f'Value of a is {a},value of b is {b}')
#multiple string values
name,place = input().split()
print(f'Value of a is {name},value of b is {place}')
names=list(map(str,input("enter the names:").split(',')))
print(names)

h=list(map(lambda x:x.upper(),['codegnan','python','data','sankar']))
print(h)

discount=list(map(lambda x: x-x*0.1,[2500,3500,4000]))
print(discount)
b=[2500,3500,4000]
c=[]
def discount(b):
    for i in b:
        i=i-i*0.1
        c.append(i)
    return c
print(discount(b))
#list Comprehensions with if-else usage
#Syntax --> [true_value if condition else false_value for expression in collection
#filter even or odd values in given range

result=["Even" if i%2==0 else "odd"  for i in range(1,21)]
print(result)

result=[i**2 if i%2==0 else i**3 for i in range(1,21)]
print(result)

#Nested loops with list comprehensions
#syntax --> [expression for item1 in iterable1 for item2 in iterable2]

colors =['Green','Red','Blue']
sizes =['s','m','l']
matching =[(i,j) for i in colors for j in sizes]
print(matching)
'''
marks = [25,25,24,20]
weekly_marks = [35,30,45,48]
final=[mark+wmark for mark in marks for wmark in weekly_marks]
print(final)

final=list(map(lambda mark,wmark:(mark+wmark),marks,weekly_marks))
print(final)
#Nested Comprehension with if-else combination
#syntax --> true_value if <condition> else false_value for item1 in iterable1 for item2 in iterable2]
f = [i+4 if i>=j else i-3 for i in range(1,5) for j in range(1,5)]
print(f)
print(*f)#it unpacks value from above collection











