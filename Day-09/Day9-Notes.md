'''
Loops
for loop:-
while loop

for loop:-
a for loop is used to iterate over a sequence ,list ,tuple
else in for loop:-

s=[1,2,3,4]
for a in s:
    print(a)
    if a==3:
       break
else:
    print("entered")
s="python is a language"
for j in s :
    print(j)
s=[1,2,3,4,5,6]
for j in s :
    print(j)
s=(1,2,3,4,5,6)
for j in s :#j is called as instance varible
    print(j)
    
s={"name":"sankar",
   "role":"not decided"}
for r in s.values():
    print(r)
s={"name":"sankar",
   "role":"not decided"}
for r in s:
    print(r)
else:
    print("program ended")
Control Statements
break
continue
pass
break:-
break is used to exit the loop
s=[1,2,3,4]
for a in s:
    print(a)
    if a==3:
       break
else:
    print("entered")
continue:-
the continue will skip the current iteration 
s=[1,2,3,4]
for a in s:
    if a==3:
     continue
    print(a)
else:
    print("entered")
pass:-
space holder
s=[1,2,3,4]
for a in s:
    pass
range():-
range()is a in-build function that is used to generate a sequence upto a limit
syntax:-
range(start,end,step)
s=[1,2,3,4]
for a in range(20,50):
print(a)

while:-
the while loop excute untill the condition becomes true
i=1
while i<5:
    print(i)
    i+=1
    '''
assert keyword:-
it will used to check the condition, but it will raise an error incase it is false...
num=int(input("enter the number:"))
assert age>18, "you must have 18 years" 

    
