#12
#Creating datetime objects
#In the datetime module, date and time can be represented as separate objects or as one. The class that combines date and time is called datetime.
#Its constructor accepts the following parameters:

#Parameter	Restrictions
#year	The year parameter must be greater than or equal to 1 (MINYEAR constant) and less than or equal to 9999 (MAXYEAR constant).

#month	The month parameter must be greater than or equal to 1 and less than or equal to 12.

#day	The day parameter must be greater than or equal to 1 and less than or equal to the last day of the given month and year.

#hour	The hour parameter must be greater than or equal to 0 and less than 23.

#minute	The minute parameter must be greater than or equal to 0 and less than 59.

#second	The second parameter must be greater than or equal to 0 and less than 59.

#microsecond	The microsecond parameter must be greater than or equal to 0 and less than 1000000.

#tzinfo	The tzinfo parameter must be a tzinfo subclass object or None (default).

#fold	The fold parameter must be 0 or 1 (default 0).

from datetime import datetime

dt = datetime(2019, 11, 5, 20, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())
>>
Datetime: 2019-11-05 20:53:00
Date: 2019-11-05
Time: 20:53:00

#The example creates a datetime object representing November 5, 2019 at 20:53:00. All parameters passed to the constructor go to read-only class attributes. They're year, month, day, hour, minute, second, microsecond, tzinfo, and fold.
#The example shows two methods that return two different objects. The method called date returns the date object with the given year, month, and day, while the method called time returns the time object with the given hour and minute.

#13
#Methods that return the current date and time
#The datetime class has several methods that return the current date and time. These methods are:

#today() — returns the current local date and time with the tzinfo attribute set to None;
#now() — returns the current local date and time the same as the today method, unless we pass the optional argument tz to it. The argument of this method must be an object of the tzinfo subclass;
#utcnow() — returns the current UTC date and time with the tzinfo attribute set to None.
from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())
>>
today: 2024-07-05 10:42:50.030418
now: 2024-07-05 10:42:50.031602
utcnow: 2024-07-05 10:42:50.031877

#As you can see, the result of all the three methods is the same. The small differences are caused by the time elapsed between subsequent calls.

#14
#Getting a timestamp
#There are many converters available on the Internet that can calculate a timestamp based on a given date and time, but how can we do it in the datetime module?
#This is possible thanks to the timestamp method provided by the datetime class.
#The timestamp method returns a float value expressing the number of seconds elapsed between the date and time indicated by the datetime object and January 1, 1970, 00:00:00 (UTC).
from datetime import datetime

dt = datetime(2020, 10, 7, 23, 55)
print("Timestamp:", dt.timestamp())
>> Timestamp: 1602114900.0

#15
#Date and time formatting (part 1)
#All datetime module classes presented so far have a method called strftime. This is a very important method, because it allows us to return the date and time in the format we specify.
#The strftime method takes only one argument in the form of a string specifying the format that can consist of directives.
#A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter, e.g., the directive %Y means the year with the century as a decimal number.
from datetime import date

d = date(2020, 1, 28)
print(d.strftime('%Y/%m/%d'))


ed = date(2023, 11, 21)
print(ed.strftime('%Y/%m/%d'))

>>
2020/01/28
2023/11/21

#a format consisting of three directives separated by / (slash) to the strftime method. Of course, the separator character can be replaced by another character, or even by a string.
#You can put any characters in the format, but only recognizable directives will be replaced with the appropriate values. In our format we've used the following directives:

#%Y – returns the year with the century as a decimal number. In our example, this is 2020.
#%m – returns the month as a zero-padded decimal number. In our example, it's 01.
#%d – returns the day as a zero-padded decimal number. In our example, it's 28.


#16
#Date and time formatting (part 2)
#Time formatting works in the same way as date formatting, but requires the use of appropriate directives.
#The first of the formats used concerns only time. As you can guess, %H returns the hour as a zero-padded decimal number, %M returns the minute as a zero-padded decimal number, while %S returns the second as a zero-padded decimal number. 
from datetime import time
from datetime import datetime

t = time(22, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 18, 23, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

>>
22:53:00
20/November/18 23:53:00

#The second format used combines date and time directives. There are two new directives, %Y and %B. The directive %Y returns the year without a century as a zero-padded decimal number (in our example it's 20). 
#The %B directive returns the month as the locale’s full name (in our example, it's November).

#17
#The strftime() function in the time module
#the strftime function is available in the time module. It differs slightly from the strftime methods in the classes provided by the datetime module because, 
#in addition to the format argument, it can also take (optionally) a tuple or struct_time object.
#If you don't pass a tuple or struct_time object, the formatting will be done using the current local time. 
import time

timestamp = 1372879119
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))
>>
2013/07/03 19:18:39
2024/07/05 11:24:4

#Creating a format looks the same as for the strftime methods in the datetime module. 

#18
#The strptime() method
#Knowing how to create a format can be helpful when using a method called strptime in the datetime class. Unlike the strftime method, it creates a datetime object from a string representing a date and time.
#The strptime method requires you to specify the format in which you saved the date and time. 
from datetime import datetime
print(datetime.strptime("2019/11/28 22:53:00", "%Y/%m/%d %H:%M:%S"))
>> 2019-11-28 22:53:00

#Note: In the time module, you can find a function called strptime, which parses a string representing a time to a struct_time object. Its use is analogous to the strptime method in the datetime class:

import time
print(time.strptime("2019/11/28 22:53:00", "%Y/%m/%d %H:%M:%S"))
>> time.struct_time(tm_year=2019, tm_mon=11, tm_mday=28, tm_hour=22, tm_min=53, tm_sec=0, tm_wday=3, tm_yday=332, tm_isdst=-1)

#19
#Date and time operations
#Sooner or later you'll have to perform some calculations on the date and time. 
#Fortunately, there's a class called timedelta in the datetime module that was created for just such a purpose.
#To create a timedelta object, just do subtraction on the date or datetime objects.
from datetime import date
from datetime import datetime

d1 = date(2020, 11, 28)
d2 = date(2019, 11, 28)

print(d1 - d2)

dt1 = datetime(2020, 11, 28, 0, 0, 0)
dt2 = datetime(2019, 11, 28, 10, 53, 0)

print(dt1 - dt2)

>>
366 days, 0:00:00
365 days, 13:07:00

#The example shows subtraction for both the date and datetime objects. In the first case, we receive the difference in days, which is 366 days. Note that the difference in hours, minutes, and seconds is also displayed. 
#In the second case, we receive a different result, because we specified the time that was included in the calculations. As a result, we receive 365 days, 9 hours, and 7 minutes.

#20
#Creating timedelta objects
#Of course, you can also create an object yourself. For this purpose, let's get acquainted with the arguments accepted by the class constructor, 
#which are: days, seconds, microseconds, milliseconds, minutes, hours, and weeks. Each of them is optional and defaults to 0.
#The arguments should be integers or floating point numbers, and can be either positive or negative.
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)
>> 16 days, 3:00:00
#The result of 16 days is obtained by converting the weeks argument to days (2 weeks = 14 days) and adding the days argument (2 days). 
#This is normal behavior, because the timedelta object only stores days, seconds, and microseconds internally. Similarly, the hour argument is converted to minutes.

from datetime import timedelta

delta = timedelta(weeks=3, days=8, hours=7)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)
>>
Days: 29
Seconds: 25200
Microseconds: 0

#The result of 25200 is obtained by converting 7 hours into seconds. In this way the timedelta object stores the arguments passed during its creation. 
#Weeks are converted to days, hours and minutes to seconds, and milliseconds to microseconds.

#21
#Creating timedelta objects: continued
#You already know how the timedelta object stores the passed arguments internally. It's time to see how it can be used in practice.
from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=3, days=7, hours=8)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 12) + delta2
print(d)

dt = datetime(2019, 10, 12, 10, 53) + delta2
print(dt)
>>
28 days, 8:00:00
56 days, 16:00:00
2019-12-07
2019-12-08 02:53:00
 
#The timedelta object can be multiplied by an integer. 
#Note that both days and hours have been multiplied by 2. Another interesting operation using the timedelta object is adding. In the example, we've added the timedelta object to the date and datetime objects.
#As a result of these operations, we receive date and datetime objects increased by days and hours stored in the timedelta object.
#The presented multiplication operation allows you to quickly increase the value of the timedelta object, while multiplication can also help you get a date from the future.
#Of course, the timedelta, date, and datetime classes support many more operations.
