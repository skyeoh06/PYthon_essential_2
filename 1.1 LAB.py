# 1.5
# Importing a module
import math
print(math.sin(math.pi/2))
>> 1.0

# 1.6
import math


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))
>>
0.99999999
1.0

# 1.8
# line 32: carry out the selective import;
# line 34: make use of the imported entities and get the expected result (1.0)
# lines 39 through 43: redefine the meaning of pi and sin - in effect, they supersede the original (imported) definitions within the code's namespace;
# line 46: get 0.99999999, which confirms our conclusions.

from math import sin, pi

print(sin(pi / 2))

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))
>>
1.0
0.99999999

# lines 56 through 63: define our own pi and sin;
# line 66: make use of them (0.99999999 appears on the screen)
# line 68: carry out the import - the imported symbols supersede their previous definitions within the namespace;
# line 70: get 1.0 as a result.
  
pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))
>>
0.99999999
1.0

# 1.9
# Importing a module: *
from module import *

# Importing a module: the as keyword
import module as alias

# 1.10
# Importing a module | aliasing
import math as m

print(m.sin(m.pi/2))
>> 1.0

from math import pi as PI, sin as sine

print(sine(PI/2))
>> 1.0

# 1.11
# invoke the function make_money() contained in the module named mint
import mint
mint.make_money()

# invoke the function make_money() contained in the module named mint
from mint import make_money
make_money()

# You've written a function named make_money on your own. You need to import a function of the same name from the mint module and don't want to rename any of your previously defined names. Which variant of the import statement may help you with the issue?
from mint import make_money as make_more_money

# What form of the make_money function invocation is valid if your code starts with the following line?
from mint import *
make_money()

