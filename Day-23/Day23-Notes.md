'''
Polymorphism:
-->it means many forms
--> it allows same method, function or operator to perform different
tasks depending on the same object...

Types:
1.Method Overloading.
-->It means having multiple methods with the same name but different parameters.

2.Method Overriding.

3.Operator overloading.
'''
class cal:
    def add(self,num,num2=0):
        print(num+num2)
    def add(self,num,num_2=0,num_3=0):
        print(num+num_2+num_3)
obj=cal()
obj.add(4,7,9)
obj.add(23,45)

2) Method Overriding :-
---------------------
the method overriding occurs when a child clss provides its own implementation of a method already defined in its parent class.....
Class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def sound(self):
        print("Dogs Bark")
d=dog()
d.sound()
        
    
3) Operator Overloading:-
This allows operators (+,-,*) to work differently for user-defined objects
1) __add__
2) __sub__
3) __mul__
class student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
s1=student(56)
s2=student(67)
print(s1 + s2)
------------------------
Data Abstraction
================
Data Abstraction is the process of hiding implementation details and showing only the essential data to the user
eg:-
ATM
CAR
APP
------------------
from abc import ABC,abstractmethod
class parent:
    @abstractmethod
    def display(self):
        pass
from abc import ABC ,abstractmethod
class bank:
    @abstractmethod
    def interest(self):
        print('SBI interest Rate: 6.5%)
class SBI(bank):
    def interst(self):
        print('HDFC Interest Rate:5.5%')
class ICIC(bank):
    def interest(self):
        print('ICIC interest Rate:6.9%')
banks =[SBI(),HDFC(),ICIC()]
for j in banks:
    j.interest()
