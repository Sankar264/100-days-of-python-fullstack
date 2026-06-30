'''
Input formatting from user
input()
The input() function is used to take input from the user ....
1.INT
num=int(input("Enter a number:"))
num_2=int(input("Enter a number:"))
print(num+num_2)
2.string
how=input("enter a char:")
print(how + 'sai')
3.float
num=float(input("enter your salary:"))
print(num, "is the monthly salary")
4.list
group=list(map(int,input().split()))
print(group)
5.tuple
group=tuple(map(int,input().split()))
print(group)
some = tuple(map(int,input().split()))
print(some)
group=tuple(input().split())
print(group)
'''
num=eval(input("enter:"))#evalute
print(type(num))
name=input("enter your name:")
age=int(input("enter your age:"))
print(name,"your age is",age)
print(f"{name} your age is {age}")#f string
print("My name is %s and i'm %d years old" %(name,age))#modulus format




