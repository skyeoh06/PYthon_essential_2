#1.2
#the function is able to:
#read a desired number of characters (including just one) from the file, and return them as a string;
#read all the file contents, and return them as a string;
#if there is nothing more to read (the virtual reading head reaches the end of the file), the function returns an empty string.
from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

#The routine is rather simple:

#use the try-except mechanism and open the file of the predetermined name (text.txt in our case)
#try to read the very first character from the file (ch = s.read(1))
#if you succeed (this is proven by a positive result of the while condition check), output the character (note the end= argument - it's important! You don't want to skip to a new line after every character!);
#update the counter (cnt), too;
#try to read the next character, and the process repeats.

#1.
