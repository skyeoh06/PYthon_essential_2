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


