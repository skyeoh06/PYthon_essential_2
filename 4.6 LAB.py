#1.2
#You will start your adventure with the calendar module with a simple function called calendar, which allows you to display the calendar for the whole year.
#The result displayed is similar to the result of the cal command available in Unix. 
#If you want to change the default calendar formatting, you can use the following parameters:

w – date column width (default 2)
l – number of lines per week (default 1)
c – number of spaces between month columns (default 6)
m – number of columns (default 3)
#The calendar function requires you to specify the year, while the other parameters responsible for formatting are optional. We encourage you to try these parameters yourself.
import calendar
print(calendar.calendar(2024))
>>
                                 2024

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                   1  2  3
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       4  5  6  7  8  9 10
15 16 17 18 19 20 21      12 13 14 15 16 17 18      11 12 13 14 15 16 17
22 23 24 25 26 27 28      19 20 21 22 23 24 25      18 19 20 21 22 23 24
29 30 31                  26 27 28 29               25 26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31

#A good alternative to the above function is the function called prcal, which also takes the same parameters as the calendar function, but doesn't require the use of the print function to display the calendar. 
import calendar
calendar.prcal(2024)
>>
                                  2024

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                   1  2  3
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       4  5  6  7  8  9 10
15 16 17 18 19 20 21      12 13 14 15 16 17 18      11 12 13 14 15 16 17
22 23 24 25 26 27 28      19 20 21 22 23 24 25      18 19 20 21 22 23 24
29 30 31                  26 27 28 29               25 26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31

#1.3
#Calendar for a specific month.
#The calendar module has a function called month, which allows you to display a calendar for a specific month. 
#As in the calendar function, you can change the default formatting using the following parameters:

w – date column width (default 2)
l – number of lines per week (default 1)
import calendar
print(calendar.month(2024, 11))
>> 
   November 2024
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30

Note: You can also use the prmonth function, which has the same parameters as the month function, but doesn't require you to use the print function to display the calendar.
import calendar
calendar.prmonth(2024, 11)
>>
   November 2024
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30

#1.4
#The setfirstweekday() function
#by default in the calendar module, the first day of the week is Monday. However, you can change this behavior using a function called setfirstweekday.
#the setfirstweekday method requires a parameter expressing the day of the week in the form of an integer value. 

import calendar

calendar.setfirstweekday(6)
calendar.prmonth(2020, 12)
>>
   December 2020
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)
>>
   December 2020
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

import calendar

calendar.setfirstweekday(2)
calendar.prmonth(2020, 12)

>>
   December 2020
We Th Fr Sa Su Mo Tu
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

#1.5
#The weekday() function
#Another useful function provided by the calendar module is the function called weekday, which returns the day of the week as an integer value for the given year, month, and day. 
import calendar
print(calendar.weekday(2020, 12, 24))
>> 3
#The weekday function returns 3, which means that December 24, 2020 is a Thursday.
import calendar
print(calendar.weekday(2024, 11, 24))
>> 6

#1.6
#The weekheader() function
#The weekheader method requires you to specify the width in characters for one day of the week. If the width you provide is greater than 3, you'll still get the abbreviated weekday names consisting of three characters.
import calendar
print(calendar.weekheader(2))
>> Mo Tu We Th Fr Sa Su

#Note: If you change the first day of the week, e.g., using the setfirstweekday function, it'll affect the result of the weekheader function.
import calendar
calendar.setfirstweekday(2)
print(calendar.weekheader(3))
>> Wed Thu Fri Sat Sun Mon Tue

#1.7
#How do we check if a year is a leap year?
#The calendar module provides two useful functions to check whether years are leap years.
#he first one, called isleap, returns True if the passed year is leap, or False otherwise. 
#The second one, called leapdays, returns the number of leap years in the given range of years.
import calendar

print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2030))
>>
True
5

#In the example, we obtain the result 3, because in the period from 2010 to 2024 there are only three leap years (note: 2024 is not included). They are the years 2012, 2016, and 2020.

