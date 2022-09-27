Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 12
x = int()
x
0
x = 12432432432423423423423
type(x)
<class 'int'>
import sys
sys.getsizeof(0)
24
sys.getsizeof(1)
28
sys.getsizeof(1212)
28
sys.getsizeof(45443543534534)
32
x = 12.434
type(x)
<class 'float'>
sys.getsizeof(x)
24
x = "hello"
x = 'hello'
x = '''hello'''
x = """hello"""
type(x)
<class 'str'>
sys.getsizeof('')
49
sys.getsizeof('a')
50
sys.getsizeof('ab')
51
sys.getsizeof('abc')
52
x = True
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
True = "hello"
SyntaxError: cannot assign to True
x
True
x = False
sys.getsizeof(x)
24
x = True
sys.getsizeof(x)
28
text = "hello how are you..?"
text.encode()
b'hello how are you..?'
text = b"hello"
type(text)
<class 'bytes'>
text.decode()
'hello'
text = "नमस्ते आप कैसे हैं ?"
text.encode()
b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82 ?'
text = text.encode()
text.decode()
'नमस्ते आप कैसे हैं ?'
x = 12
x = [4,3,4,6,8,5,4,78,23,34]
type(x)
<class 'list'>
x = (4,3,4,6,8,5,4,78,23,34)
type(x)
<class 'tuple'>
x = {"name" : "Ram", "age" : 34, "dept" : "IT"}
type(x)
<class 'dict'>
x = {3,2,5,3,4,67,12,12,4,6,8,4,4,7,9,0,1}
x
{0, 1, 2, 67, 3, 4, 5, 6, 8, 7, 9, 12}
