Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
t.shape("turtle")
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
for i in range(4):
    print("Hello...")

    
Hello...
Hello...
Hello...
Hello...
for i in range(4):
    print(i)

    
0
1
2
3
t.reset()
for i in range(4):
    t.forward(200)
    t.left(90)

    
t.reset()
for i in range(50):
    t.forward(4 * i)
    t.left(45)

    
t.reset()
for i in range(20):
    t.circle(4 * i)
    t.left(45)

    
t.reset()
t.speed(0)
for i in range(50):
    t.circle(4 * i)
    t.left(45)

    

== RESTART: C:/Users/asus/OneDrive/Desktop/New folder/for_loop_demo.py =
0
1
2
3
4

== RESTART: C:/Users/asus/OneDrive/Desktop/New folder/for_loop_demo.py =
0,1,2,3,4,

== RESTART: C:/Users/asus/OneDrive/Desktop/New folder/for_loop_demo.py =
0,1,2,3,4,
2,3,4,5,6,7,8,9,10,

== RESTART: C:/Users/asus/OneDrive/Desktop/New folder/for_loop_demo.py =
0,1,2,3,4,
2,3,4,5,6,7,8,9,10,
2,4,6,8,10,12,14,16,18,20,

== RESTART: C:/Users/asus/OneDrive/Desktop/New folder/for_loop_demo.py =
0,1,2,3,4,
2,3,4,5,6,7,8,9,10,
2,4,6,8,10,12,14,16,18,20,

== RESTART: C:/Users/asus/OneDrive/Desktop/New folder/for_loop_demo.py =
0,1,2,3,4,
2,3,4,5,6,7,8,9,10,
2,4,6,8,10,12,14,16,18,20,
10
9
8
7
6
5
4
3
2

== RESTART: C:/Users/asus/OneDrive/Desktop/New folder/for_loop_demo.py =
0,1,2,3,4,
2,3,4,5,6,7,8,9,10,
2,4,6,8,10,12,14,16,18,20,
10,9,8,7,6,5,4,3,2,
import turtle
t = turtle.Pen()
t.shape("turtle")
x = 100
while x > 0:
    t.circle(x * 4)
    x = x - 3
    t.left(x)

    
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    t.circle(x * 4)
  File "C:\Python310\lib\turtle.py", line 1992, in circle
    self._go(l)
  File "C:\Python310\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Python310\lib\turtle.py", line 3181, in _goto
    self._update()
  File "C:\Python310\lib\turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python310\lib\turtle.py", line 565, in _delay
    self.cv.after(delay)
  File "C:\Python310\lib\tkinter\__init__.py", line 834, in after
    self.tk.call('after', ms)
KeyboardInterrupt
t.reset()
x = 1
t.speed(0)
while x < 100:
    t.circle(x * 4)
    x += 3
    t.left(x)

    
x
100
