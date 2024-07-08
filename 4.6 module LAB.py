#1.9
#Creating a Calendar object
#The Calendar class constructor takes one optional parameter named firstweekday, by default equal to 0 (Monday).
import calendar  

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")
>> 0 1 2 3 4 5 6 

The firstweekday parameter must be an integer between 0-6.

import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
>> 6 0 1 2 3 4 5 

#The code example uses the Calendar class method named iterweekdays, which returns an iterator for week day numbers.
#The first value returned is always equal to the value of the firstweekday property. 

#1.10
#The itermonthdates() method
#The Calendar class has several methods that return an iterator. One of them is the itermonthdates method, which requires specifying the year and month.
#As a result, all days in the specified month and year are returned, as well as all days before the beginning of the month or the end of the month that are necessary to get a complete week.
#Each day is represented by a datetime.date object.
import calendar  

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
>>
2019-10-28 2019-10-29 2019-10-30 2019-10-31 2019-11-01 2019-11-02 2019-11-03 2019-11-04 2019-11-05 2019-11-06 2019-11-07 2019-11-08 2019-11-09 2019-11-10 2019-11-11 2019-11-12 2019-11-13 2019-11-14 2019-11-15 2019-11-16 
2019-11-17 2019-11-18 2019-11-19 2019-11-20 2019-11-21 2019-11-22 2019-11-23 2019-11-24 2019-11-25 2019-11-26 2019-11-27 2019-11-28 2019-11-29 2019-11-30 2019-12-01 

#The code displays all days in November 2019. Because the first day of November 2019 was a Friday, the following days are also returned to get the complete week: 10/28/2019 (Monday) 10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 10/31/2019 (Thursday).
#The last day of November 2019 was a Saturday, so in order to keep the complete week, one more day is returned 12/01/2019 (Sunday).

#1.11
#Other methods that return iterators
#Another useful method in the Calendar class is the method called itermonthdates, which takes year and month as parameters, and then returns the iterator to the days of the week represented by numbers.
import calendar  

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
>> 0 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 0 

#You’ll have certainly noticed the large number of 0s returned as a result of the example code. These are days outside the specified month range that are added to keep the complete week.
#The first four zeros represent 10/28/2019 (Monday) 10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 10/31/2019 (Thursday). The remaining numbers are days in the month, except the last value of 0, which replaces the date 12/01/2019 (Sunday).
#There are four other similar methods in the Calendar class that differ in data returned:

itermonthdates2 – returns days in the form of tuples consisting of a day of the month number and a week day number;
itermonthdates3 – returns days in the form of tuples consisting of a year, a month, and a day of the month numbers. This method has been available since version 3.7;
itermonthdates4 – returns days in the form of tuples consisting of a year, a month, a day of the month, and a day of the week numbers. This method has been available since Python version 3.7.

import calendar  

c = calendar.Calendar()

for iter in c.itermonthdates(2019, 11):
    print(iter, end=" ")

>> 2019-10-28 2019-10-29 2019-10-30 2019-10-31 2019-11-01 2019-11-02 2019-11-03 2019-11-04 2019-11-05 2019-11-06 2019-11-07 2019-11-08 2019-11-09 2019-11-10 2019-11-11 2019-11-12 2019-11-13 2019-11-14 2019-11-15 
2019-11-16 2019-11-17 2019-11-18 2019-11-19 2019-11-20 2019-11-21 2019-11-22 2019-11-23 2019-11-24 2019-11-25 2019-11-26 2019-11-27 2019-11-28 2019-11-29 2019-11-30 2019-12-01 

#1.12
#The monthdays2calendar() method
#the monthdays2calendar method, which takes the year and month, and then returns a list of weeks in a specific month. Each week is a tuple consisting of day numbers and weekday numbers. 
#Note that the days numbers outside the month are represented by 0, while the weekday numbers are a number from 0-6, where 0 is Monday and 6 is Sunday.
import calendar  

c = calendar.Calendar()

for data in c.monthdays2calendar(2024, 7):
    print(data)
>>
[(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)]
[(8, 0), (9, 1), (10, 2), (11, 3), (12, 4), (13, 5), (14, 6)]
[(15, 0), (16, 1), (17, 2), (18, 3), (19, 4), (20, 5), (21, 6)]
[(22, 0), (23, 1), (24, 2), (25, 3), (26, 4), (27, 5), (28, 6)]
[(29, 0), (30, 1), (31, 2), (0, 3), (0, 4), (0, 5), (0, 6)]


#1.13
#Create a class called MyCalendar that extends the Calendar class;
#create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
#in your implementation, use the monthdays2calendar method of the Calendar class.
#The following are the expected results:

#Sample arguments

#year=2019, weekday=0
#Expected output

#52

#Sample arguments
##year=2000, weekday=6
#Expected output

#53
import calendar  

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self,year,weekday):
        month =1
        number_of_occurrences = 0
        while month<= 12:
            for data in self.monthdays2calendar(year,month):
                if (data[weekday][0]) > 0:
                    number_of_occurrences +=1  
            month+=1 
        return number_of_occurrences
my_calendar=MyCalendar()
print(my_calendar.count_weekday_in_year(2024,6))
print(my_calendar.count_weekday_in_year(2019,0))
print(my_calendar.count_weekday_in_year(2000,5))
>>
52
52
53

#1.14
#What is the output of the following snippet?

import calendar
print(calendar.weekheader(1))
>> M T W T F S S

#What is the output of the following snippet?

import calendar  

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")

>> 0 1 2 3 4 5 6



