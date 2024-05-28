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

# Step 5 :
