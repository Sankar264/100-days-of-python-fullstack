#prime number check
num=10
count=0
for j in range (1,num+1) :
 if num % j == 0:
     count+=1
     print(count)
if count==2:
    print(num,"is a prime")
else:
    print(num,"is not a prime")
#
n=10
for j in range(1,n+1):
    count==0
    for i in range(1,j+1):
        if j%i==0:
            count+=1 
    if count==2:
        print(num,"is a prime")
#
num=5
for j in range(1,num+1):
    for i in range(1,j+1):
        print("*",end = " ")
    print()
num=5
for j in range(1,num+1):
    for i in range(1,j+1):
        print(j,end = " ")
    print()
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i,end = " ")
    print()
num=5
count=0
for j in range(1,num+1):
    for i in range(1,j+1):
        count+=1
        print(count,end = " ")
    print()
#armstrong number
a=153
len=len(str(a))
sum=0
for j in str(a):
    sum+=int(j)**len
if sum==a:
    print(f"{a} is armstrong")
else:
    print(f"{a} is not")

num=6
for j in range(num):
    print(" "*(num-j-1),end=" ")
    print("*"*(2*j+1))


    
      
      
            
      
    
