'''
---------------lambda function--------------
this is also called annonymous function.
a lambda function can take n number of arguments but having only one expression
syntax--->
lambda arguments :expression
some=lambda an : an+5
print(some(10))

some=lambda an,so,why : an + so + why
print(some(10,5,9))
filter()
the filter() function is a built in function used to filter elements from an itterables such as list,tuple and set based on condition
syntax:-
filter(function,itterable)
this is filter() function returns filter object so we can convert that into other types list,set,tuple
'''
nums=[1,2,3,4,5]
rev=filter(lambda a:a%2 == 0,nums)
print(tuple(rev))
nums=[1,2,3,4,5]
rev=filter(lambda a:a%2 != 0,nums)
print(tuple(rev))
----------------list comprehension------------------------
this offers shorter syntax when we want to create new list from the old list
syntax:-variable_name = [expression loop condition]
old = [1,2,3,4,5]
new = [j for j in old if j%2==0]
print(new)
-----------------dictionary comprehension---------------
This offers a shorter syntax when we want to create a new dict from the old dict
syntax:-variable_name = [expression loop]
old__dict={1:2,3:4,5:6}
new_dict={i:j for i in old_dict.items() if j%2==0}
print(new_dict)


