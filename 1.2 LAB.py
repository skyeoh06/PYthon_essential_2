# 1.1
# Useful Modules
# dir(module)
# The function returns an alphabetically sorted list containing all entities' names available in the module identified by a name passed to the function as an argument
import math

for name in dir(math):
    print(name, end="\t")
>>
__doc__	__file__	__loader__	__name__	__package__	__spec__	acos	acosh	asin	asinh	atan	
tan2	atanh	ceil	copysign	cos	cosh	degrees	e	erf	erfc	exp	expm1	fabs	
factorial	floor	fmod	frexp	fsum	gamma	gcd	hypot	inf	isclose	isfinite	isinf	isnan	ldexp	
lgamma	log	log10	log1p	log2	modf	nan	pi	pow	radians	sin	sinh	sqrt	tan	tanh	tau	trunc

# execute the function directly in the Python console (IDLE)
import math
dir(math)

# 1.2
# Selected functions from the math module
# The first group of the math's functions are connected with trigonometry:

# sin(x) → the sine of x;
# cos(x) → the cosine of x;
# tan(x) → the tangent of x.
# there are also their inversed versions:

# asin(x) → the arcsine of x;
# acos(x) → the arccosine of x;
# atan(x) → the arctangent of x.
# To effectively operate on angle measurements
# pi → a constant with a value that is an approximation of π;
# radians(x) → a function that converts x from degrees to radians;
# degrees(x) → acting in the other direction (from radians to degrees)
# hyperbolic analogues:

# sinh(x) → the hyperbolic sine;
# cosh(x) → the hyperbolic cosine;
# tanh(x) → the hyperbolic tangent;
# asinh(x) → the hyperbolic arcsine;
# acosh(x) → the hyperbolic arccosine;
# atanh(x) → the hyperbolic arctangent.

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
>> True
print(ar == pi / 2.)
>> True
print(sin(ar) / cos(ar) == tan(ar))
>> True
print(asin(sin(ar)) == ar)
>> True

# 1.3
# exponentiation:

# e → a constant with a value that is an approximation of Euler's number (e)
# exp(x) → finding the value of ex;
# log(x) → the natural logarithm of x
# log(x, b) → the logarithm of x to base b
# log10(x) → the decimal logarithm of x (more precise than log(x, 10))
# log2(x) → the binary logarithm of x (more precise than log(x, 2))
# Note: the pow() function:

# pow(x, y) → finding the value of xy (mind the domains)
# This is a built-in function, and doesn't have to be imported.

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
>> False
print(pow(2, 2) == exp(2 * log(2)))
>> True
print(log(e, e) == exp(0))
>> True

# 1.4
# The last group consists of some general-purpose functions like:

# ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
# floor(x) → the floor of x (the largest integer less than or equal to x)
# trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
# factorial(x) → returns x! (x has to be an integral and not a negative)
# hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise)

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
>> 1 2
print(floor(-x), floor(-y))
>> -2 -3
print(ceil(x), ceil(y))
>> 2 3
print(ceil(-x), ceil(-y))
>> -1 -2
print(trunc(x), trunc(y))
>> 1 2
print(trunc(-x), trunc(-y))
>> -1 -2

# 1.6
# Selected functions from the random module
# The random function

# The most general function named random() (not to be confused with the module's name) produces a float number x coming from the range (0.0, 1.0) - in other words: (0.0 <= x < 1.0).

from random import random

for i in range(5):
    print(random())
>>
0.3509905039912684
0.022168116687638517
0.17748895399515097
0.13700007053046104
0.6029927976084677

# The seed function

# The seed() function is able to directly set the generator's seed. We'll show you two of its variants:

# seed() - sets the seed with the current time;
# seed(int_value) - sets the seed with the integer value int_value.
# Due to the fact that the seed is always set with the same value, the sequence of generated values always looks the same.

from random import random, seed

seed(0)

for i in range(5):
    print(random())
>>
0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335
0.5112747213686085

# 1.7
# The randrange and randint functions

# If you want integer random values, one of the following functions would fit better:

# randrange(end)
# randrange(beg, end)
# randrange(beg, end, step)
# randint(left, right)
# The first three invocations will generate an integer taken (pseudorandomly) from the range (respectively):

# range(end)
# range(beg, end)
# range(beg, end, step)
# Note the implicit right-sided exclusion!

# The last function is an equivalent of randrange(left, right+1) - it generates the integer value i, which falls in the range [left, right] (no exclusion on the right side).
from random import randrange, randint

print(randrange(1), end=' ')
>> 0
print(randrange(0, 1), end=' ')
>> 0
print(randrange(0, 1, 1), end=' ')
>> 0
print(randint(0, 1))
>> 0

# 1.8
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')
>>
6,5,4,4,3,4,10,7,10,7,
10,7,5,5,5,8,1,1,5,10,

# The choice and sample functions
# It's a function named in a very suggestive way - choice:

# choice(sequence)
# sample(sequence, elements_to_choose)
# The first variant chooses a "random" element from the input sequence and returns it.

# The second one builds a list (a sample) consisting of the elements_to_choose element "drawn" from the input sequence.

# In other words, the function chooses some of the input elements, returning a list with the choice. The elements in the sample are placed in random order. Note: the elements_to_choose must not be greater than the length of the input sequence.

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
>> 7
print(sample(my_list, 5))
>> [9, 2, 4, 6, 8]
print(sample(my_list, 10))
>> [5, 10, 6, 3, 1, 4, 9, 7, 8, 2]

# 1.10
# Selected functions from the platform module
# The platform function

# The platform module lets you access the underlying platform's data, i.e., hardware, operating system, and interpreter version information.

# There is a function that can show you all the underlying layers in one glance, named platform, too. It just returns a string describing the environment; thus, its output is rather addressed to humans than to automated processing (you'll see it soon).

# This is how you can invoke it:

# platform(aliased = False, terse = False)
# aliased → when set to True (or any non-zero value) it may cause the function to present the alternative underlying layer names instead of the common ones;
# terse → when set to True (or any non-zero value) it may convince the function to present a briefer form of the result (if possible)
from platform import platform

print(platform())
>> Linux-4.4.0-210-generic-x86_64-with
print(platform(1))
>> Linux-4.4.0-210-generic-x86_64-with
print(platform(0, 1))
>> Linux-4.4.0-210-generic-x86_64-with

# 1.11
# Selected functions from the platform module
# The machine function
# Sometimes, you may just want to know the generic name of the processor which runs your OS together with Python and your code - a function named machine() will tell you that. As previously, the function returns a string.
from platform import machine

print(machine())
>> x86_64

# 1.12
# Selected functions from the platform module
# The processor function
# The processor() function returns a string filled with the real processor name (if possible).
from platform import processor

print(processor())
>> x86

# 1.13
# Selected functions from the platform module
# The system function
# A function named system() returns the generic OS name as a string.
from platform import system

print(system())
>> Linux

# 1.14
# Selected functions from the platform module
# The version function
# The OS version is provided as a string by the version() function.
from platform import version

print(version())
>> #242-Ubuntu SMP Fri Apr 16 09:57:56 UTC 2021

# 1.15
# Selected functions from the platform module
# The python_implementation and the python_version_tuple functions
# If you need to know what version of Python is running your code, you can check it using a number of dedicated functions - here are two of them:

# python_implementation() → returns a string denoting the Python implementation (expect CPython here, unless you decide to use any non-canonical Python branch)

# python_version_tuple() → returns a three-element tuple filled with:
# the major part of Python's version;
# the minor part;
# the patch level number.
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
>>
CPython
3
7
10

# 1.17
# What is the expected value of the result variable after the following code is executed?
import math
result = math.e == math.exp(1)
>> True

# (Complete the sentence) Setting the generator's seed with the same value each time your program is run guarantees that...
>> ... the pseudo-random values emitted from the random module will be exactly the same.

# Which of the platform module's functions will you use to determine the name of the CPU running inside your computer?
>> The processor() function

# What is the expected output of the following snippet?

import platform
print(len(platform.python_version_tuple()))
>> 3
