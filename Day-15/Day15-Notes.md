
nums=[23,4,6,23,7,4]
empty=[]
def removes(nums,empty):
    for j in nums:
        if j not in empty:
            empty.append(j)
    print(empty)
removes(nums,empty)

nums=int(input())
count=0
def func(nums,count):
    for j in range(1,nums+1):
        if nums%j==0 :
            count+=1
    if count==2:
        print("prime number")
    else:
        print("not prime number")
func(nums,count)

s="python is a programming language"
count=0
def counting(s,count):
    do=s.split(  )
    for j in do:
        count+=1
    print(count)
counting(s,count)
#count upper an lower characters

string = input("enter your sentence: ")
cap_count = 0
small_count = 0
space_count = 0
def cap_small(string,cap_count,small_count,space_count):
    for i in string:
        if i.isupper():
            cap_count += 1
        elif i.islower():
            small_count += 1
        else:
            space_count += 1
    print(f" there are total {cap_count} number caps")
    print(f" there are total {small_count} number caps")
    print(f" there are total {space_count} number caps")
cap_small(string,cap_count,small_count,space_count)
        
    
        
            
