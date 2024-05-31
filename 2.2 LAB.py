# 1.1
# Example 1
# The len() function used for strings returns a number of characters contained by the arguments. hn 

word = 'by'
print(len(word))
>> 2

# Example 2
# Any string can be empty. Its length is 0.

empty = ''
print(len(empty))
>> 0

# Example 3
# a backslash (\) used as an escape character is not included in the string's total length. 

i_am = 'I\'m'
print(len(i_am))
>> 3

# 1.2
# Multiline strings
multiline = '''Line #1
Line #2'''

print(len(multiline))
>> 15
# Line #1 contains seven characters. Two such lines comprise 14 characters. 
# The missing character is simply invisible - it's a whitespace. It's located between the two text lines.
# It's denoted as: \n.
# The multiline strings can be delimited by triple quotes, too.

# 1.3
# Operations on strings
# In general, strings can be:

# concatenated (joined)
# replicated
# The ability to use the same operator against completely different kinds of data (like numbers vs. strings) is called overloading (as such an operator is overloaded with different duties).
# The + operator used against two or more strings produces a new string containing all the characters from its arguments (note: the order matters - this overloaded +, in contrast to its numerical version, is not commutative).
str1 = 'a'
str2 = 'b'

print(str1 + str2)
>> ab
print(str2 + str1)
>> ba
print(5 * 'a')
>> aaaaa
print('b' * 4)
>> bbbb

# 1.4
# Operations on strings: ord()
# To know a specific character's ASCII/UNICODE code point value, you can use a function named ord() (as in ordinal).
# The function needs a one-character string as its argument - breaching this requirement causes a TypeError exception, and returns a number representing the argument's code point.
# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
>> 97
print(ord(char_2))
>> 32

# 1.5
# Operations on strings: chr()
# The function takes a code point and returns its character.
# Invoking it with an invalid argument (e.g., a negative or invalid code point) causes ValueError or TypeError exceptions.
# Demonstrating the chr() function.

print(chr(97))
>> a
print(chr(945))
>> α

# 1.6
# Strings as sequences: indexing
# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()
>> s i l l y   w a l k s 

# Strings as sequences: iterating
# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()
>> s i l l y   w a l k s 

# 1.7
# Slices
alpha = "abdefg"

print(alpha[1:3])
>> bd
print(alpha[3:])
>> efg
print(alpha[:3])
>> abd
print(alpha[3:-2])
>> e
print(alpha[-3:4])
>> e
print(alpha[::2])
>> adf
print(alpha[1::2])
>> beg

# 1.8
# The in and not in operators
# The in operator
# The in operator shouldn't surprise you when applied to strings - it simply checks if its left argument (a string) can be found anywhere within the right argument (another string).
# The result of the check is simply True or False.
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
>> True
print("F" in alphabet)
>> False
print("1" in alphabet)
>> False
print("ghi" in alphabet)
>> True
print("Xyz" in alphabet)
>> False

# The not in operator
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
>> False
print("F" not in alphabet)
>> True
print("1" not in alphabet)
>> True
print("ghi" not in alphabet)
>> False
print("Xyz" not in alphabet)
>> True

# 1.9
# Python strings are immutable
#doesn't allow you to use the del instruction to remove anything from a string.
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Write test code here.
del alphabet[0]
>> TypeError: 'str' object doesn't support item deletion

# The only thing you can do with del and a string is to remove the string as a whole. 
del alphabet
>> 

# Python strings don't have the append() method
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Write test code here.
alphabet.append("A")
>> AttributeError: 'str' object has no attribute 'append'

# the insert() method is illegal
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Write test code here.
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.insert(0, "A")
>> AttributeError: 'str' object has no attribute 'insert'

# 1.10
# Operations on strings
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)
>> abcdefghijklmnopqrstuvwxyz

# 1.11
#Operations on strings: min()
#The function finds the minimum element of the sequence passed as an argument. There is one condition - the sequence (string, list, it doesn't matter) cannot be empty, or else you'll get a ValueError exception.
#Recall the ASCII table
# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))
>> A

# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')
>> [ ]
t = [0, 1, 2]
print(min(t))
>> 0

# 1.12
# Operations on strings: max()
a function named max() finds the maximum element of the sequence.
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))
>> v

# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')
>> [y]
t = [0, 1, 2]
print(max(t))
>> 2

# 1.13
# Operations on strings: the index() method
# The index() method (it's a method, not a function) searches the sequence from the beginning, in order to find the first element of the value specified in its argument.
# Note: the element searched for must occur in the sequence - its absence will cause a ValueError exception.
# The method returns the index of the first occurrence of the argument (which means that the lowest possible result is 0, while the highest is the length of argument decremented by 1).
# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
>> 2
print("aAbByYzZaA".index("Z"))
>> 7
print("aAbByYzZaA".index("A"))
>> 1

# 1.14
# Operations on strings: the list() function
# The list() function takes its argument (a string) and creates a new list containing all the string's characters, one per list element.
# Note: it's not strictly a string function - list() is able to create a new list from many other entities (e.g., from tuples and dictionaries).

# Demonstrating the list() function:
print(list("abcabc"))
>> ['a', 'b', 'c', 'a', 'b', 'c']

# Operations on strings: the count() method
# The count() method counts all occurrences of the element inside the sequence. The absence of such elements doesn't cause any problems.
# Demonstrating the count() method:
print("abcabc".count("b"))
>> 2
print('abcabc'.count("d"))
>> 0

# 1.15
# What is the length of the following string assuming there is no whitespaces between the quotes?

"""
"""
>> 1

print(len("\n\n"))
>> 2

# What is the expected output of the following code?

s = 'yesteryears'
the_list = list(s)
print(the_list[3:6])
>> ['t', 'e', 'r']

# What is the expected output of the following code?

for ch in "abc":
    print(chr(ord(ch) + 1), end='')
>> bcd

