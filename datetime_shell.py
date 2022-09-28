Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time
time.ctime
<built-in function ctime>
time.ctime()
'Wed Sep 28 18:21:10 2022'
import calendar
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

import datetime
datetime.datetime.now()
datetime.datetime(2022, 9, 28, 18, 22, 22, 848831)
print(datetime.datetime.now())
2022-09-28 18:22:33.758845
d = datetime.datetime.now().date()
t = datetime.datetime.now().time()
print(d)
2022-09-28
print(t)
18:22:50.614329
d.strftime("%d/%m/%y")
'28/09/22'
d.strftime("%d %b,%y")
'28 Sep,22'
d.strftime("%d %B,%y")
'28 September,22'
d.strftime("%d %B, %Y")
'28 September, 2022'
d.strftime("%d %B, %Y, %p")
'28 September, 2022, AM'
d.strftime("%d %B, %Y, %a")
'28 September, 2022, Wed'
d.strftime("%d %B, %Y, %A")
'28 September, 2022, Wednesday'
t.strftime("%H:%M:%S")
'18:22:50'
t.strftime("%H:%M:%S, %p")
'18:22:50, PM'
t.strftime("%I:%M:%S, %p")
'06:22:50, PM'
t.strftime("%I:%M:%S, %p")
'06:22:50, PM'
t = datetime.datetime.now().time()
t.strftime("%I:%M:%S, %p")
'06:25:14, PM'
