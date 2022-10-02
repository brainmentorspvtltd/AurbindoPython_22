Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def counter():
    x = 0
    while True:
        x += 1
        return x

    
counter()
1
counter()
1
counter()
1
x = 0
def counter():
    while True:
        x += 1
        return x

    
counter()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    counter()
  File "<pyshell#11>", line 3, in counter
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
def counter():
    x = 0
    while True:
        x += 1
        return x

    
counter()
1
counter()
1
counter()
1
def counter():
    x = 0
    while True:
        x += 1
        yield x

        
counter()  # generator
<generator object counter at 0x0000022749ED5770>
# iterator - we are going to iterate on / we are going to perform loop
count = counter()
next(count)
1
next(count)
2
next(count)
3
next(count)
4
next(count)
5
def greet():
    print("Hello")
    yield "Hey User"
    print("Bye")
    yield "Take Care"

    
greet()
<generator object greet at 0x0000022749ED5770>
gen = greet()
next(gen)
Hello
'Hey User'
next(gen)
Bye
'Take Care'
next(gen)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    next(gen)
StopIteration
