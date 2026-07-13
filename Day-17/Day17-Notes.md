'''                                                #Modules#

--> A module is a python file(.py) that contains resuable code
1.variable
2.Funtions
3.classes
4.objects
5.statements

Why this
--------
-->Insead of writing the same code repeatedly, we can store it is a module and use it wheneever needed...

Types of modules:
----------------
1.user-defined

import modules
print(modules.add(23,45))

2.built-in
-math:
-------
-->create a new folder and execute the operations.
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2,3))
print(math.pi)
print(math.sin(90))

-os:
---
-->os module is used to intract with the os to make file and to delete fille.
import os
print(os.getcwd())
os.mkdier("sai")
os.rmdir("sai")

-sys:
-----
--->this is provide the information about python interpeter
import sys
print(sys.version)

-random:
--------
-->used to generate random values


'''
import random
print(random.randint(15,25))

colors = ["yellow","red","blue","green"]
print(random.choice(colors))
