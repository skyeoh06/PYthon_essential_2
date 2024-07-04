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

#1.3
#If you're absolutely sure that the file's length is safe and you can read the whole file to the memory at once, you can do it - 
#the read() function, invoked without any arguments or with an argument that evaluates to None, will do the job for you.
#Remember - reading a terabyte-long file using this method may corrupt your OS.
from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
>>
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Characters in file: 131

#Let's analyze it:

#open the file as previously;
#read its contents by one read() function invocation;
#next, process the text, iterating through it with a regular for loop, and updating the counter value at each turn of the loop;

#1.4
#Processing text files: readline()
#If you want to treat the file's contents as a set of lines, not a bunch of characters, the readline() method will help you with that.
#The method tries to read a complete line of text from the file, and returns it as a string in the case of success. Otherwise, it returns an empty string.
#This opens up new opportunities - now you can also count lines easily, not only characters.
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
>>
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Characters in file: 131
Lines in file:      4

#1.5
#Processing text files: readlines()
#Another method, which treats text file as a set of lines, not characters, is readlines().
#The readlines() method, when invoked without arguments, tries to read all the file contents, and returns a list of strings, one element per file line.
#If you're not sure if the file size is small enough and don't want to test the OS, you can convince the readlines() method to read not more than a specified number of bytes at once (the returning value remains the same - it's a list of a string).
#The maximum accepted input buffer size is passed to the method as its argument.
#You may expect that readlines() can process a file's contents more effectively than readline(), as it may need to be invoked fewer times.
#Note: when there is nothing to read from the file, the method returns an empty list. Use it to detect the end of the file.
#To the extent of the buffer's size, you can expect that increasing it may improve input performance, but there is no golden rule for it - try to find the optimal values yourself.
#Look at the code in the editor. We've modified it to show you how to use readlines().
#We've decided to use a 15-byte-long buffer. Don't think it's a recommendation.
#We've used such a value to avoid the situation in which the first readlines() invocation consumes the whole file.
#We want the method to be forced to work harder, and to demonstrate its capabilities.
#There are two nested loops in the code: the outer one uses readlines()'s result to iterate through it, while the inner one prints the lines character by character.
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
>>
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Characters in file: 131
Lines in file:      4

#modified code
from os import strerror

try:
    s = open("text.txt")
    print(s.readlines(20))
    print(s.readlines(20))
    print(s.readlines(20))
    print(s.readlines(20))
    s.close()
    
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
>>
['Beautiful is better than ugly.\n']
['Explicit is better than implicit.\n']
['Simple is better than complex.\n']
['Complex is better than complicated.']

#1.6
#The last example we want to present shows a very interesting trait of the object returned by the open() function in text mode.
#We think it may surprise you - the object is an instance of the iterable class.
#The iteration protocol defined for the file object is very simple - its __next__ method just returns the next line read in from the file.
#Moreover, you can expect that the object automatically invokes close() when any of the file reads reaches the end of the file.
from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
>>
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Characters in file: 131
Lines in file:      4

#1.7
#Dealing with text files: write()
#Writing text files seems to be simpler, as in fact there is one method that can be used to perform such a task.
#The method is named write() and it expects just one argument - a string that will be transferred to an open file (don't forget - 
#the open mode should reflect the way in which the data is transferred - writing a file opened in read mode won't succeed).
#No newline character is added to the write()'s argument, so you have to add it yourself if you want the file to be filled with a number of lines.
#The example in the editor shows a very simple code that creates a file named newtext.txt (note: the open mode w ensures that the file will be created from scratch, even if it exists and contains data) and then puts ten lines into it.
#The string to be recorded consists of the word line, followed by the line number. We've decided to write the string's contents character by character (this is done by the inner for loop) but you're not obliged to do it in this way.
#We just wanted to show you that write() is able to operate on single characters.
from os import strerror

try:
	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

>>
The code creates a file filled with the following text:

line #1
line #2
line #3
line #4
line #5
line #6
line #7
line #8
line #9
line #10

#1.8
#We've modified the previous code to write whole lines to the text file.
#The contents of the newly created file are the same.
#Note: you can use the same method to write to the stderr stream, but don't try to open it, as it's always open implicitly.
#For example, if you want to send a message string to stderr to distinguish it from normal program output, it may look like this:

import sys
sys.stderr.write("Error message")

from os import strerror

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


#1.10
#Bytearrays resemble lists in many respects. For example, they are mutable, they're a subject of the len() function, and you can access any of their elements using conventional indexing.
#There is one important limitation - you mustn't set any byte array elements with a value which is not an integer (violating this rule will cause a TypeError exception) 
#and you're not allowed to assign a value that doesn't come from the range 0 to 255 inclusive (unless you want to provoke a ValueError exception).
#You can treat any byte array elements as integer values - just like in the example in the editor.
#Note: we've used two methods to iterate the byte arrays, and made use of the hex() function to see the elements printed as hexadecimal values.
#Now we're going to show you how to write a byte array to a binary file - binary, as we don't want to save its readable representation - we want to write a one-to-one copy of the physical memory content, byte by byte.
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

>>
0xa
0x9
0x8
0x7
0x6
0x5
0x4
0x3
0x2
0x1

#1.11
#Look at the code in the editor. Let's analyze it:

#first, we initialize bytearray with subsequent values starting from 10; if you want the file's contents to be clearly readable, replace 10 with something like ord('a') - 
#this will produce bytes containing values corresponding to the alphabetical part of the ASCII code (don't think it will make the file a text file - it's still binary, as it was created with a wb flag);
#then, we create the file using the open() function - the only difference compared to the previous variants is the open mode containing the b flag;
#the write() method takes its argument (bytearray) and sends it (as a whole) to the file;
#the stream is then closed in a routine way.
#The write() method returns a number of successfully written bytes.
#If the values differ from the length of the method's arguments, it may announce some write errors.
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

#How to read bytes from a stream
#Reading from a binary file requires use of a specialized method name readinto(), as the method doesn't create a new byte array object, but fills a previously created one with the values taken from the binary file.

#Note:
#the method returns the number of successfully read bytes;
#the method tries to fill the whole space available inside its argument; if there are more data in the file than space in the argument, the read operation will stop before the end of the file; otherwise, 
#the method's result may indicate that the byte array has only been filled fragmentarily (the result will show you that, too, and the part of the array not being used by the newly read contents remains untouched)
from os import strerror

data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

>> 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 

#Let's analyze it:

#first, we open the file (the one you created using the previous code) with the mode described as rb;
#then, we read its contents into the byte array named data, of size ten bytes;
#finally, we print the byte array contents - are they the same as you expected?

#1.12
#An alternative way of reading the contents of a binary file is offered by the method named read().
#Invoked without arguments, it tries to read all the contents of the file into the memory, making them a part of a newly created object of the bytes class.
#This class has some similarities to bytearray, with the exception of one significant difference - it's immutable.
#Fortunately, there are no obstacles to creating a byte array by taking its initial value directly from the bytes object.
#Be careful - don't use this kind of read if you're not sure that the file's contents will fit the available memory.
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

>> 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 

#1.13
#If the read() method is invoked with an argument, it specifies the maximum number of bytes to be read.
#The method tries to read the desired number of bytes from the file, and the length of the returned object can be used to determine the number of bytes actually read.
from os import strerror

data = bytearray(ord('a'))

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(8))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
>> 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11





