Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 12
x + 5
17
x - 6
6
x / 7
1.7142857142857142
x * 45
540
x // 7
1
22 / 7
3.142857142857143
22 // 7
3
2 ** 5
32
2 ** 20
1048576
2 ** 10
1024
2 *** 3
SyntaxError: invalid syntax
2 ** 3
8
x = 12
print("Hello","World")
Hello World
print("Hello","World",sep='-')
Hello-World
print("Hello","World",sep='+')
Hello+World
x
12
x += 5
x
17
x -= 2
x
15
x *= 4
x
60
x = 12
y = 20
x > y
False
x < y
True
x == y
False
x >= y
False
x <= y
True
x != y
True
x
12
y
20
z = 25
x > y and x > z
False
y > x and y > z
False
z > x and z > y
True
y > x or y > z
True
x is not y
True
text = "Hello how are you...?"
"hello" in text
False
"Hello" in text
True
x = [3,2,5,7,78,23,56,8]
10 in x
False
5 in x
True
5 not in x
False
x = 12
y = 12
id(x)
1192017920592
id(12)
1192017920592
id(y)
1192017920592
id(12)
1192017920592
x is y
True
x = "hello how are you"
y = "hello how are you"
x == y
True
x is y
False
id(x)
1192054880208
id(y)
1192054879968
1 | 5
5
1 | 5
5
1 | 4
5
3 & 4
0
