'''
#passing by value
def some(a):
    for j in a:
        print(j)
some([1,2,3])
#return keyword:-
in a function if  return is excuted then it will be exit from the function with certain values
def myfunc(b):
    return 5+b
a=myfunc(10)
c=myfunc(100)
print(a)
print(c)
'''
import builtins

builtin_functions =[
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}")
----------------recursive function--------------------------
recursive function that calls itself repeated untill a specific condition is met..
syntax
def func_name(parameter):
    if condition: -->base case
    return statement
    else:
        return statement
print(func_name(arguments))

def func_name(num):
    if num==1:
        return 1
    else:
        return num * func_name(num-1)
num = 1
print(func_name(num)) 33 
