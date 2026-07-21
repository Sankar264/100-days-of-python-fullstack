'''
#-----------------------Day-25------------------------
ErrorHandling
for j in range(1,10:
    print(j)
o/p---Syntax Error
for j in range(1,10)
    print(j)
else:
print()

   a=20
for j in range(a):
    print(j)
else:
print()
#o/p --- IndenticationError
Value Error
-----------
num=int(input("Enter a num:"))
o/p -- ValueError
num=int(input("Enput a num:"))
o/p -- ValueError

The try block will test the code for error
syntax:--try
except:-
-----------
This except let us handle the errors in the code

finally

try:
    num = int(input("Enter a num:"))
except NameError:
    print('will get name error')


try:
    num = int(input("Enter a num:"))
except ValueError:
    print('will get name error')
 
try:
    num = int(input("Enter a num:"))
    num_2= int(input("Enter a  num:"))
    print(num/num_2)
except :
    print('will get zerodivison Error')
except ValueError:
    print('will get name error')
else:
    print('no error')
else:-
-----

if the try block block does not have any error than the else block will execute
'''
finally:-
The finally block will execute either code contain errors or not
eg:-
try:
    num = int(input("Enter a num:"))
    num_2= int(input("Enter a  num:"))
    print(num/num_2)
except ZeroDivisionError:
    print('will get zerodivison Error')
except ValueError:
    print('will get name error')
else:
    print('no error')
finally :
    print('end')



