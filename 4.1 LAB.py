#1.1
#Generators
for i in range(5):
    print(i)

>>
0
1
2
3
4


#1.2
#The iterator protocol is a way in which an object should behave to conform to the rules imposed by the context of the for and in statements. 
#An object conforming to the iterator protocol is called an iterator.
#An iterator must provide two methods:

#__iter__() which should return the object itself and which is invoked once (it's needed for Python to successfully start the iteration)
#__next__() which is intended to return the next value (first, second, and so on) of the desired series - it will be invoked by the for/in statements in order to pass through the next iteration; 
#if there are no more values to provide, the method should raise the StopIteration exception.

class Fib:
    #the class constructor prints a message (use this to trace the class's behavior), prepares some variables (__n to store the series limit, 
    #__i to track the current Fibonacci number to provide, and __p1 along with __p2 to save the two previous numbers);
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1
    
    #the __iter__ method is obliged to return the iterator object itself; 
    #one of its components is an iterator able to scan the collection; the __iter__ method should extract the iterator and entrust it with the execution of the iteration protocol;
    #the method starts its action by printing a message;
    def __iter__(self):
        print("__iter__")
        return self
    #the __next__ method is responsible for creating the sequence;
    #first, it prints a message, then it updates the number of desired values, and if it reaches the end of the sequence, 
    #the method breaks the iteration by raising the StopIteration exception
    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)

>>
__init__
__iter__
__next__
1
__next__
1
__next__
2
__next__
3
__next__
5
__next__
8
__next__
13
__next__
21
__next__
34
__next__
55
__next__

#1.3
#built the Fib iterator into another class (we can say that we've composed it into the Class class). It's instantiated along with Class's object.
class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter;


object = Class(8)

for i in object:
    print(i)

>>
Class iter
1
1
2
3
5
8
13
21

#1.5
# a generator to produce the first n powers of 2
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

>>
1
2
4
8
16
32
64
128

#List comprehensions
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = [x for x in powers_of_2(5)]
print(t)

>> [1, 2, 4, 8, 16]

#The list() function
#The list() function can transform a series of subsequent generator invocations into a real list.
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = list(powers_of_2(3))
print(t)
>> [1, 2, 4]

#The in operator
#the context created by the in operator allows you to use a generator
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for i in range(20):
    if i in powers_of_2(4):
        print(i)
>>
1
2
4
8

#The Fibanacci number generator
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)
>> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



