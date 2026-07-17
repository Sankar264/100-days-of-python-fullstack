'''
Day-22
-----------
Inheritence
===========
Inheritence is an OOPS concept where one class (child /derived) acquired the properties and methods of another class (parent/base)

Class Parent:
    pass
class child(parent):
    pass
1) Single Inheritence
--------------------
A child class inherits from parent is single inheritence

class animal:
    def sound(self):
        print('Animals make sounds')
class dog(animal):
    def barks(self):
        print("Dog Barks")
d=dog()
d.sound()
d.barks()

#multiple Inheritance:
#--------------------------
#Achild inherits more than one parent is called
class gfather:
    def stalam(self):
        print('1 ar sold by rohith gfather for 500')
class rohith:
    def bharat(self):
        print('rohith becomes begger because of gfather')
class father:
    def land(self):
        print('rohith bokka petadanikii valla thata la codegnan join ayaduu')

s=son()
s.bharat()
s.land()
s.flat

#MultiLevel
-----------
one child class becomes the parent for another class
class gfather:
    def house(self):
        print('OWNS HOUSE')
class father(gfather):
    def flat(self):
        print('NEW 3BHK FLAT')
class son(father):
    def car(self):
        print('Have a car')
fam=son()
fam.house()
fam.flat()
----------------------------

hierachical
-------------------------
class kgfmother:
    def gold(self):
        print('ada')
class rocky(kgfmother):
    def garuda(self):
        print('dadaa')
class adira(kgfmother):
    def vikings(self):
        print('cahadaa')
child_1=rocky()
child_2=adira()

child_1.gold()
child_1.garuda()

child_2.gold()
child_2.vikings()

Hybrid
------------------

This is the combination of two or more types of inheritance
example of multiple+multilevel

class A:
    def methodA(self):
        print('class A')
class B(A):
    def methodB(self):
        print('class B')
class C(A):
    def methodC(self):
        print('class C')
class D(B,C):
    def methodD(self):
        print('class D')
S=D()
S.methodA()
S.methodB()
S.methodC()

Super()
-------------
This super() function is used to access the parent class methods or constructor in the child class.....
'''
class parent:
    def show(self):
        print('parent method')
class child(parent):
    def show(self):
        super().show()
        print('child class')
chi=child()
chi.show()

class person:
    def __init__(self,name):
        self.name=name
class student:
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def display(self):
        print(self.name)
        print(self.roll)
a=student('Sankar',202)
a.display()

    
