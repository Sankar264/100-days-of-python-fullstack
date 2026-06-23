Python Day-2

Type of operators:-

· Arithmetic operators :-It is used for mathematical operations
  eg:- +,-,%,//,/,**
    a=10
    b=20
    print(a+b)
· Assignment operators :-specialized symbols used to assign the evaluation result of a right-hand expression to a variable on the left-hand side
  eg:- =,+=,-=,*=
   a=20
   a=+20 #a=*4 
   print(a)
· Comparison operators :-Comparison operators in Python evaluate the relationship between two values and always return a Boolean result
  eg:-<,>,==,<=,>=
  a=20         
  b=30
  print(a==b)
  a=20
  b=30
  print(a!=b)
  a=20
  b=30
  print(a<=b)
· Logical operators :- 
  eg:- and :-returns true if both are true
       eg:-a=20
           b=7
           c=89
           print(a<=b and c>=a)
       or:- return true if any one is true
           a=20
           b=7
           c=89
           print(a<=b or c>=a)
      not:-reverser the output
· Identity operators :- used to compare the memory locations of two objects to determine if they are the exact same instance in memory
    is=same object or not
    a=20
    b=30
    print(a==b)
    print(a is b)
    is not=not the same object
· Membership operators :-Python uses membership operators to test if a specific value or variable exists within a data sequence 
  in:-The in operator in Python evaluates to True if the specified value or variable is found inside the data sequence
  a=[1,2,3,4,5]
  print(20 in a)
  not in:-The not in operator is a Python membership operator used to verify the absence of an element.
  a=[1,2,3,4,5]
  print(20 not in a)

· Bitwise operators:-Bitwise operators evaluate integer values directly at the binary (base-2) level, comparing individual 1s and 0s
   eg:-&,<<,>>
   print(3|4)
   print(5&4)
