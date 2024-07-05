#2
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

