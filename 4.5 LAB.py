#1.2
#Getting the current local date and creating date objects
#One of the classes provided by the datetime module is a class called date. Objects of this class represent a date consisting of the year, month, and day. 
#Look at the code in the editor to see what it looks like in practice and get the current local date using the today method.
#The today method returns a date object representing the current local date. Note that the date object has three attributes: year, month, and day.

from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
>>
Today: 2024-07-05
Year: 2024
Month: 7
Day: 5


#To create a date object, you must pass the year, month, and day parameters.
from datetime import date

my_date = date(2024, 11, 24)
print(my_date)
>> 2024-11-24

#When creating a date object, keep the following restrictions in mind:
#Parameter	Restrictions
#year	
#The year parameter must be greater than or equal to 1 (MINYEAR constant) and less than or equal to 9999 (MAXYEAR constant).

#month	
#The month parameter must be greater than or equal to 1 and less than or equal to 12.

#day	
#The day parameter must be greater than or equal to 1 and less than or equal to the last day of the given month and year.

#1.3
#Creating a date object from a timestamp
#The date class gives us the ability to create a date object from a timestamp.
#In Unix, the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC). This date is called the Unix epoch, because this is when the counting of time began on Unix systems.
#The timestamp is actually the difference between a particular date (including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds.
#To create a date object from a timestamp, we must pass a Unix timestamp to the fromtimestamp method.
#For this purpose, we can use the time module, which provides time-related functions. One of them is a function called time() that returns the number of seconds from January 1, 1970 to the current moment in the form of a float number. 
#If you run the sample code several times, you'll be able to see how the timestamp increments itself. 
#It's worth adding that the result of the time function depends on the platform, because in Unix and Windows systems, leap seconds aren't counted.
from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

>>
Timestamp: 1720163569.3532252
Date: 2024-07-05
Timestamp: 1720163695.8952346
Date: 2024-07-05
Timestamp: 1720163709.2737105
Date: 2024-07-05
Timestamp: 1720163711.66383
Date: 2024-07-05
Timestamp: 1720163719.4709303
Date: 2024-07-05
Timestamp: 1720163724.1445205
Date: 2024-07-05
Timestamp: 1720163726.5250392
Date: 2024-07-05

#1.4
#Creating a date object using the ISO format
#The datetime module provides several methods to create a date object. One of them is the fromisoformat method, which takes a date in the YYYY-MM-DD format compliant with the ISO 8601 standard.
#The ISO 8601 standard defines how the date and time are represented. It's often used, so it's worth taking a moment to familiarize yourself with it. Take a look at the picture describing the values required by the format:
YYYY-MM-DD
#When substituting the date, be sure to add 0 before a month or a day that is expressed by a number less than 10.
from datetime import date

d = date.fromisoformat('2023-11-08')
print(d)
>> 2023-11-08

#1.5
#The replace() method
#Sometimes you may need to replace the year, month, or day with a different value. 
from datetime import date

d = date(2009, 2, 5)
print(d)

d = d.replace(year=2024, month=11, day=16)
print(d)

y = d.replace(year=2021)
print(y)

m = y.replace(month=8)
print(m)

t = m.replace(day=29)
print(t)

>>
2009-02-05
2024-11-16
2021-11-16
2021-08-16
2021-08-29

#replace method, e.g., year, or all three as in the example.
#The replace method returns a changed date object, so you must remember to assign it to some variable.

#1.6
#What day of the week is it?
#One of the more helpful methods that makes working with dates easier is the method called weekday. 
#It returns the day of the week as an integer, where 0 is Monday and 6 is Sunday. 
from datetime import date

d = date(1981, 11, 24)
print(d.weekday())
>> 1

#The date class has a similar method called isoweekday, which also returns the day of the week as an integer, but 1 is Monday, and 7 is Sunday.
from datetime import date

d = date(1981, 11, 24)
print(d.isoweekday())
>> 2

#As you can see, for the same date we get a different integer, but expressing the same day of the week. The integer returned by the isodayweek method follows the ISO 85601 specification.

#1.7
#Creating time objects
#You already know how to present a date using the date object. The datetime module also has a class that allows you to present time. Can you guess its name? Yes, it's called time:

#time(hour, minute, second, microsecond, tzinfo, fold)

#The time class constructor accepts the following optional parameters:

#Parameter	Restrictions
#hour	  The hour parameter must be greater than or equal to 0 and less than 23.

#minute	 The minute parameter must be greater than or equal to 0 and less than 59.

#second	 The second parameter must be greater than or equal to 0 and less than 59.

#microsecond	The microsecond parameter must be greater than or equal to 0 and less than 1000000.

#tzinfo	The tzinfo parameter must be a tzinfo subclass object or None (default).

#fold	  The fold parameter must be 0 or 1 (default 0).

#The tzinfo parameter is associated with time zones, while fold with wall times. We won't use them during this course, but we encourage you to familiarize yourself with them.
#In the example, we passed four parameters to the class constructor: hour, minute, second, and microsecond. Each of them can be accessed using the class attributes.
from datetime import time

t = time(12, 53, 22, 8)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

>>
Time: 12:53:22.000008
Hour: 12
Minute: 53
Second: 22
Microsecond: 8

#1.8
#The time module
#In addition to the time class, the Python standard library offers a module called time, which provides a time-related function. You already had the opportunity to learn the function called time when discussing the date class. 
#Now we'll look at another useful function available in this module.
import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(10)
>>
I'm very tired. I have to take a nap. See you later.
I slept well! I feel great!

#The most important part of the sample code is the use of the sleep function (yes, you may remember it from one of the previous labs earlier in the course), which suspends program execution for the given number of seconds.
#Extend the student's sleep by changing the number of seconds. Note that the sleep function accepts only an integer or a floating point number.

#1.9
#The ctime() function
#The time module provides a function called ctime, which converts the time in seconds since January 1, 1970 (Unix epoch) to a string.
import time

timestamp = 1578879180
print(time.ctime(timestamp))
>> Mon Jan 13 01:33:00 2020

#The ctime function returns a string for the passed timestamp. 
#It's also possible to call the ctime function without specifying the time in seconds.
import time
print(time.ctime())
>> Fri Jul  5 08:05:45 2024

#1.10
#The gmtime() and localtime() functions
#Some of the functions available in the time module require knowledge of the struct_time class, but before we get to know them, let's see what the class looks like:

#time.struct_time:
    tm_year   # specifies the year
    tm_mon    # specifies the month (value from 1 to 12)
    tm_mday   # specifies the day of the month (value from 1 to 31)
    tm_hour   # specifies the hour (value from 0 to 23)
    tm_min    # specifies the minute (value from 0 to 59)
    tm_sec    # specifies the second (value from 0 to 61 )
    tm_wday   # specifies the weekday (value from 0 to 6)
    tm_yday   # specifies the year day (value from 1 to 366)
    tm_isdst  # specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
    tm_zone   # specifies the timezone name (value in an abbreviated form)
    tm_gmtoff # specifies the offset east of UTC (value in seconds)


#The struct_time class also allows access to values using indexes. Index 0 returns the value in tm_year, while 8 returns the value in tm_isdst.
#The exceptions are tm_zone and tm_gmoff, which cannot be accessed using indexes.

import time

timestamp = 1682899988
print(time.gmtime(timestamp))
print(time.localtime(timestamp))
>>
time.struct_time(tm_year=2023, tm_mon=5, tm_mday=1, tm_hour=0, tm_min=13, tm_sec=8, tm_wday=0, tm_yday=121, tm_isdst=0)
time.struct_time(tm_year=2023, tm_mon=5, tm_mday=1, tm_hour=0, tm_min=13, tm_sec=8, tm_wday=0, tm_yday=121, tm_isdst=0)

#The example shows two functions that convert the elapsed time from the Unix epoch to the struct_time object. 
#The difference between them is that the gmtime function returns the struct_time object in UTC, while the localtime function returns local time. For the gmtime function, the tm_isdst attribute is always 0.

#1.11
#The asctime() and mktime() functions
#The time module has functions that expect a struct_time object or a tuple that stores values according to the indexes presented when discussing the struct_time class. 

import time

timestamp = 1572785580
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 3, 12, 53, 0, 0, 308, 0)))
>>
Sun Nov  3 12:53:00 2019
1572785580.0

#The first of the functions, called asctime, converts a struct_time object or a tuple to a string. Note that the familiar gmtime function is used to get the struct_time object. If you don't provide an argument to the asctime function, the time returned by the localtime function will be used.
#The second function called mktime converts a struct_time object or a tuple that expresses the local time to the number of seconds since the Unix epoch. In our example, we passed a tuple to it, which consists of the following values:

2019 => tm_year
11 => tm_mon
3 => tm_mday
12 => tm_hour
53 => tm_min
0 => tm_sec
0 => tm_wday
308 => tm_yday
0 => tm_isdst




