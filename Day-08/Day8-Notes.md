'''
Statements:-
1.conditional statements
if
if-else
nested if
elif

if :-
used to check the condition true or not
num=9  #first it should satify the first condition
if num % 2==0 :
    print(num,"is a even number")
num=9  #first it should satify the first condition
if-else:-
else is the fall-back statement incase the if condition is false this else will be excuted....
num=int(input("enter a number:")
if num % 2==0 :
    print(num,"is a even number")
else :
    print(num,"is  odd number")
example:-

sankar_icic_details={"ATM PIN" : '9090'}
pin=input("Enter your 4 digit ATM pin :")
if pin in sankar_icic_details['ATM PIN']:
        print("welcome to atm")
else :
        print("incorrect")
nested if:-
if inside the another if is called nested if
eg:-

sankar_icic_details={"ATM PIN" : '9090'}
pin=input("Enter your 4 digit ATM pin :")
if len(pin)==4:
    if pin in sankar_icic_details['ATM PIN']:
        print("welcome to atm")
    else :
        print("incorrect")
else:
    print("pls entered only 4 digit pin")
elif :-

example
num=int(input("enter the number:"))
if num>=90:
    print("A+")
elif num>=80:
    print("A")
elif num>=70:
    print("b+")
elif num>=60:
    print("D")
else :
    print("failed")
    '''
s=input("enter the alphabet:")
if s in "AEIOUaeiou" :
    print(s,"is a vowel")
else :
    print(s,"is a consonent")
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    print(a,"is greater than bc")
elif b>a and b>c :
    print(b,"is greater than ac")
elif c>a and c>b :
    print(c, "is greater than ab")
    


        

    
    
     
