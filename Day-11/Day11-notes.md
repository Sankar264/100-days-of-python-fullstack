'''
s="madam"
k=""
for i in s:
    k=i+k
    print(k)
if k==s:
    print("palindrome")
else:
    print("not")
#fabinocci series
a=0
b=1
s=int(input("enter a number"))
print(a,b,end=" ")
for i in range(1,s+1):
    all=a+b
    a=b
    b=all
    print(all,end=" ")

a=90
b=99
user=int(input("enter: \n1.add \n2.sub \n3.mul \n4.div \n5.power \n6.root\n"))
if user ==1:
    print(a+b)
elif user==2:
    print(a-b)
elif user==3:
    print(a*b)
elif user==4:
    print(a/b)
elif user==5:
    print(a**b)
elif user==4:
    print((a+b)**1/2)
else:
    print("enter correct number:")
a=19
for i in range(1,11) :
    print(a,"x",i,"=",a*i)
#perfect number
a=int(input("enter a number"))
b=0
for j in range(1,a):
    if a%j==0:
        b+=j
if b == a:
    print("perfect",a)
else:
    print("not",a)
'''
a={"name" : "sankar",
   "atm_pin":"9090",
   "balance":6000000}
print("---------------welcome to atm----------")
pin=input("enter your pin:")
if len(pin)==4 :
    if pin in a['atm_pin'] :
        choices=int(input(print("\n1withdraw \n2deposit \n3balance\n")))
        if choices==1 :
            withdraw_m=int(input("enter the withdraw amount:"))
            if withdraw_m<=a['balance'] and withdraw_m%100==0 :
                print("The amount is successfull",a['balance'])
            else:
                print("enter correct amount")
    else:
        print("enter correct pin")
else:
    print("please enter 4 digits only")
                
                      
    

