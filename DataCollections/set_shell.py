Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = {}
type(x)
<class 'dict'>
x = {3,4,6,7,8,4,5,7,2,4,6,8,5,3,12,34,6,8,3,5,7,9}
x
{2, 3, 4, 5, 6, 7, 8, 34, 9, 12}
y = {3,4,67,78,3,12,45,67,79,34,5,7,8,13}
y
{34, 67, 3, 4, 5, 7, 8, 12, 45, 78, 79, 13}
x & y
{34, 3, 4, 5, 7, 8, 12}
x | y
{2, 3, 4, 5, 6, 7, 8, 9, 67, 12, 13, 78, 79, 34, 45}
x - y
{9, 2, 6}
y - x
{67, 13, 45, 78, 79}
x.intersection(y)
{34, 3, 4, 5, 7, 8, 12}
x.union(y)
{2, 3, 4, 5, 6, 7, 8, 9, 67, 12, 13, 78, 79, 34, 45}
x.difference(y)
{9, 2, 6}
x.add(100)
x
{2, 3, 4, 5, 6, 7, 8, 34, 9, 100, 12}
x = frozenset([33,4,3,2,3,5,6])
x
frozenset({33, 2, 3, 4, 5, 6})
x[0]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x[0]
TypeError: 'frozenset' object is not subscriptable
