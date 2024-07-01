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

#1.6
#list comprehension - a simple and very impressive way of creating lists and their content.
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
>> [1, 10, 100, 1000, 10000, 100000]
print(list_2)
>> [1, 10, 100, 1000, 10000, 100000]

#1.7
#conditional expression - a way of selecting one of two different values based on the result of a Boolean expression.
#expression_one if condition else expression_two
#The value it provides is equal to expression_one when the condition is True, and expression_two otherwise.

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)
>> [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

#1.8
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)
>> [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

#turns a list comprehension into a generator:
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()
>> 1 0 1 0 1 0 1 0 1 0 

for v in the_generator:
    print(v, end=" ")
print()
>> 1 0 1 0 1 0 1 0 1 0 

print(len(the_list))
>> 10
print(len(the_generator))
>> print(len(the_generator))
TypeError: object of type 'generator' has no len()

for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()
>> 1 0 1 0 1 0 1 0 1 0 

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()
>> 1 0 1 0 1 0 1 0 1 0 

#1.9
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))
>>
4 4
1 1
0 0
1 1
4 4

#1.10
#How to use lambdas and what for?
#The most interesting part of using lambdas appears when you can use them in their pure form - as anonymous parts of code intended to evaluate a result.
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)
>>
f(-2)=18
f(-1)=8
f(0)=2
f(1)=0
f(2)=2

#efining the poly() function as lambda
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
>>
f(-2)=18
f(-1)=8
f(0)=2
f(1)=0
f(2)=2


#1.15
#What is the expected output of the following code?

class Vowels:
    def __init__(self):
        self.vow = "aeiouy "  # Yes, we know that y is not always considered a vowel.
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]


vowels = Vowels()
for v in vowels:
    print(v, end=' ')
>> a e i o u y

#Write a lambda function, setting the least significant bit of its integer argument, and apply it to the map() function to produce the string 1 3 3 5 on the console.

any_list = [1, 2, 3, 4]
even_list = # Complete the line here.
print(even_list)

>> list(map(lambda n: n | 1, any_list))

#What is the expected output of the following code?

def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement


stars = replace_spaces()
print(stars("And Now for Something Completely Different"))
>> And*Now*for*Something*Completely*Different



