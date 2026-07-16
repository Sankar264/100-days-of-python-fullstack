'''
Day-21
Self Keyword
-------------------------------

class Test:
    def display(self):
        print(self)
te=Test()
print(te)
te.display()
------------------------------
Constructor:-
==============================
This constructor initilizes the object automatically when it is created...

class batch:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def display(self):
        print(self.name)
        print(self.branch)
B4=batch('Sankar','CSE')
B4.display()

class fam:
    def __init__(self):
        self._name="sankar"
f=fam()
print(f._name)
class batch:
    def __init__(self,name,branch):
        self._name=name
        self.branch=branch
    def display(self):
        print(self._name)
        print(self.branch)
B4=batch('Sankar','CSE')
B4.display()
'''
class bank:
    def __init__(self):
        self.__pin='6600'
    def display(self):
        print(self.__pin)
AC =bank()
AC.display()
print(AC._bank__pin)
#Encapsulation:- Means wrapping the data and methods into a single
#unit(class) while controlling access to the data
class atm:
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
        self._balance+=amount
        print(self._balance)
tran=atm(balance=int(input("enter amount:")))
tran.deposit(amount=int(input("enter amount:")))


