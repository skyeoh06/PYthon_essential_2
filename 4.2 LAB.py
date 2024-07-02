#1.11
import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)


#here is a function that can dramatically simplify the error handling code.
#Its name is strerror(), and it comes from the os module and expects just one argument - an error number.
from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))


#1.12
#How do you encode an open() function’s mode argument value if you're going to create a new text file to only fill it with an article?
>> "wt" or "w"

#What is the meaning of the value represented by errno.EACCES?
>> Permission denied: you're not allowed to access the file's contents.

#What is the expected output of the following code, assuming that the file named file does not exist?

import errno

try:
    stream = open("file", "rb")
    print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")
>> absent
