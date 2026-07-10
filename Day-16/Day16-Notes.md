'''
generators
this generator is special function that returns the itertor .instead of returning all the values at once....
here we are going to use yield keyword
'
def some():
    yield 1
    yield 2
    yield 3
so = some()
print(next(so))
print(next(so))
print(next(so))

Working of generator
When a function is called
It does not execute the function immediatly...
It will the generator object
Then the function will pause at each yield..
When the next() is called again, execution resumes from where it stopped
'''
def demo():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("End")
    yield 3
how=demo()
print(next(how))
print(next(how))
print(next(how))

def how(so):
    for i in range (so):
        yield i*i
any=how(5)
print(next(any))
print(next(any))
print(next(any))
print(next(any))
print(next(any))

without generator
def sqt(n):
    for j in range(n):
        print(j*j)
sqt(5)


function
*return
*return complete result
*function will end after the return the values
*more memory usage
*this function never resume
generator
*yeild
*return one value at once
*less memory usage
*resumes after next()

yield keyword
*This will produce the value
*But the yield pause the function
*and yield will save the functions current state
*yield will continue where it stoped....
def how(so):
    for i in range (so):
        yield i*i
next() keyword
*the next() function is used to retrive the next value from a generator
StopIteration
calling next() function after all values retrive than it will raise
stopitertion exception
def how(so):
    for i in range (so):
        yield i*i
any_=how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
