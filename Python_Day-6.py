'''
OOP:-Object Oriented Programming --> Objects

POP:-Procedure Oriented programming --> Functions

#Chair(object) --> Wood (Materials),Design (Dimensions),person

A class is a blueprint of a object

A object is a real world entity which contains --> Attributes (variables)
                                               -->Methods(Functions)
class Keyword
Flipkart --> products --> laptop,mobiles,gadgets.......

Features --> Encapsulation,Inheritence,Polymorphism

#function --> house
#class --> Power House

class ClassName:
    """docstring"""
    #attributes (define the data)
    .....
    .....
    def fname(self): #behaviour
    def __init__(self):
        statement(s)...
        ..............
obj = ClassName()

#students ---> name,age
class Students:
    """Student Details"""
    Name="sankar"
    age=20
    place="Vizag"

    def details(self):
        print(f'{self.Name} is in {self.place} and age of {self.age} years')
#Creation of objects
st1 = Students()
print(st1)
print(dir(st1))
print(st1.Name,st1.age,st1.place)
#print(st1.details())#Type Error
#print(st1.details())#Name Error as we thrown self but no reference
st1.details()
st2 = Students()
st2.details()

#In above case how many objects u create the result will be same
class Students:
    """Student details for multiple Students"""
    def details(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    #now to access those details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1=Students()
st1.details("sankar",20,"Vizag")
print(st1.name,st1.place)
st1.display()
print(st1.__class__)
print(st1.__doc__)
print(st1.__dict__)
st2=Students()
st2.details("qwerty",20,"hyd")
st2.display()
print(st2.__dict__)

#In this case we want object to be initialized --> __init__()
class Students:
    """Student details for multiple Students"""
    def __init__(self,name,age,place):#constructor:-con the class
        self.name=name#instance varibles
        self.age=age
        self.place=place
    #now to access those details
    def display(self): #instance method 
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1 = Students("ekanth",25,"Hyd")
st1.display()
st2 = Students("Srinu",24,"vizag")
st2.display()
print(st2.__dict__)

#Create a cars class with attributes as brand,name,price
#create multiple objects
class cars:
    """car details for multiple cars"""
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
    def display(self):
        print(f'brand name is {self.name}')
        print(f'car brand is {self.brand} and price is {self.price}')
car1= cars("AUDI","A5",2000000)
car1.display()
car2=cars("BMW","M5",70000000)
car2.display()
car3=cars("buggati","789s",800000000)
car3.display()
#Encapsulation --> How the methods and attributes are binded to single class, in similar way how we can access the data --> Public,Protected,Private
#Public Attributes --> can be created and modified even outside the class
class Users:
    """usage of public attributes"""
    def __init__(self,username):
        self.user = username#Public attribute
    def display(self):
        print(f'Username is {self.user}')
u1=Users("sankar")
print(u1.user)
u1.user="sam"
print(u1.user)
u1.display()
#Protected Attribute --> These can also be modified outside the class, its mainly useful as a hint/coding convention for other users/developers to create a protected to create a
#protected attribute we use underscore --> _otp
class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp):
        self.user=username #public attribute
        self._otp=_otp #protected Attribute
    def display(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')
u1 = Users("Sankar",5656)
u1.display()
u1._otp = 4545
u1.display()
'''
#Private Attribute --> restrict the usage and cannot be directly accessed
#we have the usage and notation as double leading underscore --> __password
class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp,__password):
        self.user=username #public attribute
        self._otp=_otp #protected Attribute
        self.__password=__password#Private attribute
    def display(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')
u1 = Users("Sankar",656,"admin123")
print(u1.user,u1._otp)
#print(u1.__password)
#in above case password can't be accessed directly  --> NameMangling
print(u1._Users__password)

#Usage of getter(),setter() methods
class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp,__password):
        self.user=username #public attribute
        self._otp=_otp #protected Attribute
        self.__password=__password#Private attribute
#usage of getter() or get() method for password
    def get_password(self):
        """getter method for password"""
        return "******"
    #usage of setter() to modify the data
    def set_password(self,new_password):
        if len(new_password) < 6:
            return 'Password length is not matching'
        else:
            self.__password = new_password
            return 'Updated password'
u1 = Users("Admin",3455,"admin")
print(u1.get_password())
print(u1.set_password("admin"))
print(u1.set_password("admin123"))
print(u1.get_password())







        
    


