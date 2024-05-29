# Step 1 : Create empty file
>>
module.py
main.py

# Step 2 : File using module
main.py
import module

# Run main.py in the IDE
# __pycache__ folder is created with module.cpython-xy.pyc file
# The name of the file is the same as your module's name (module here). 
# The part after the first dot says which Python implementation has created the file (CPython here) and its version number. 
# The last part (pyc) comes from the words Python and compiled.
# x and y are digits derived from your version of Python.

# Step 3 : write in module.py
module.py
print("I like to be a module.")

Run module.py
output >> I like to be a module.

# Step 4 : Run main.py
output >> I like to be a module.

# Note: the initialization takes place only once

# Step 5 : Write in module.py
module.py
print("I like to be a module.")
print(__name__)
>>
I like to be a module
__main__

# run the main.py file.
>> 
I like to be a module
module

# Step 6 : 
# make use of the __main__ variable in order to detect the context in which your code has been activated
module.py
if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")
>> I prefer to be a module.

# Step 7 :
# Create counter to indicate hoow many time function being invoked
module.py
counter = 0

if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")

# Step 8 :
# Access counter in main.py
main.py
import module
print(module.counter)

# Step 9 : First Module
#!/usr/bin/env python3 

""" module.py - an example of a Python module """

__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

#used the __name__ variable to detect when the file is run stand-alone, and seized this opportunity to perform some simple tests.
if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)

# Step 10 : Update used module
main.py
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

# Step 11 : How Python searches for modules
#The variable is named path, and it's accessible through the module named sys. This is how you can check its regular value:
import sys

for p in sys.path:
    print(p)

>>
C:\Users\user
C:\Users\user\AppData\Local\Programs\Python\Python36-32\python36.zip
C:\Users\user\AppData\Local\Programs\Python\Python36-32\DLLs
C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib
C:\Users\user\AppData\Local\Programs\Python\Python36-32
C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages

# Step 12 : Access module
main.py
from sys import path

path.append('..\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
#use an absolute path, like this:
path.append('C:\\Users\\user\\py\\modules')
or use insert()
