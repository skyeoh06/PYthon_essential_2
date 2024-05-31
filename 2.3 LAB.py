# 1.1 
# The capitalize() method
# The capitalize() method does exactly what it says - it creates a new string filled with characters taken from the source string, but it tries to modify them in the following way:
# if the first character inside the string is a letter (note: the first character is an element with an index equal to 0, not just the first visible character), it will be converted to upper-case;
# all remaining letters from the string will be converted to lower-case.
# Don't forget that:
# the original string (from which the method is invoked) is not changed in any way (a string's immutability must be obeyed without reservation)
# the modified (capitalized in this case) string is returned as a result - if you don't use it in any way (assign it to a variable, or pass it to a function/method) it will disappear without a trace.
# Demonstrating the capitalize() method:
print('aBcD'.capitalize())
>> Abcd
print("Alpha".capitalize())
>> Alpha
print('ALPHA'.capitalize())
>> Alpha
print(' Alpha'.capitalize())
>>  alpha
print('123'.capitalize())
>> 123
print("αβγδ".capitalize())
>> Αβγδ
print("βαγδ".capitalize())
>> Βαγδ

# 1.2
# The center() method
# The one-parameter variant of the center() method makes a copy of the original string, trying to center it inside a field of a specified width.
# The centering is actually done by adding some spaces before and after the string.
# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
>> [  alpha   ]
print('[' + 'Beta'.center(2) + ']')
>> [Beta]
print('[' + 'Beta'.center(4) + ']')
>> [Beta]
print('[' + 'Beta'.center(6) + ']')
>> [ Beta ]
#The two-parameter variant of center() makes use of the character from the second argument, instead of a space. 
print('[' + 'gamma'.center(20, '*') + ']')
>> [*******gamma********]

# 1.3
# The endswith() method
# The endswith() method checks if the given string ends with the specified argument and returns True or False, depending on the check result.
# Note: the substring must adhere to the string's last character - it cannot just be located somewhere near the end of the string.
# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
>> yes
t = "zeta"
print(t.endswith("a"))
>> True
print(t.endswith("A"))
>> False
print(t.endswith("et"))
>> False
print(t.endswith("eta"))
>> True

# 1.4
#The find() method
# The find() method is similar to index(), which you already know - it looks for a substring and returns the index of first occurrence of this substring, but:
# it's safer - it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
# it works with strings only - don't try to apply it to any other sequence.
# Demonstrating the find() method:
print("Eta".find("ta"))
>> 1
print("Eta".find("mma"))
>> -1
# Note: don't use find() if you only want to check if a single character occurs within a string - the in operator will be significantly faster.

t = 'theta'
print(t.find('eta'))
>> 2
print(t.find('et'))
>> 2
print(t.find('the'))
>> 0
print(t.find('ha'))
>> -1

#perform the find, not from the string's beginning, but from any position, you can use a two-parameter variant of the find() method.
#The second argument specifies the index at which the search will be started (it doesn't have to fit inside the string).
print('kappa'.find('a', 2))
>> 4

#use the find() method to search for all the substring's occurrences.
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
>>
15
80
198
221
238

# a three-parameter mutation of the find() method - the third argument points to the first index which won't be taken into consideration during the search (it's actually the upper limit of the search).
print('kappa'.find('a', 1, 4))
>> 1
print('kappa'.find('a', 2, 4))
>> -1

# 1.5
# The isalnum() method
# The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.
# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
>> True
print('lambda'.isalnum())
>> True
print('30'.isalnum())
>> True
print('@'.isalnum())
>> False
print('lambda_30'.isalnum())
>> False
print(''.isalnum())
>> False
t = 'Six lambdas'
print(t.isalnum())
>> False

t = 'ΑβΓδ'
print(t.isalnum())
>> True

t = '20E1'
print(t.isalnum())
>> True

# 1.6
# The isalpha() method
# The isalpha() method is more specialized - it's interested in letters only.
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
>> True
print('Mu40'.isalpha())
>> False

# The isdigit() method
# In turn, the isdigit() method looks at digits only - anything else produces False as the result.
# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
>> True
print("Year2019".isdigit())
>> False

# 1.7
# The islower() method
# The islower() method is a fussy variant of isalpha() – it accepts lower-case letters only.
# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
>> False
print('moooo'.islower())
>> True

# The isspace() method
# The isspace() method identifies whitespaces only – it disregards any other character (the result is False then).
# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
>> True
print(" ".isspace())
>> True
print("mooo mooo mooo".isspace())
>> False

# The isupper() method
# The isupper() method is the upper-case version of islower() – it concentrates on upper-case letters only.
# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
>> False
print('moooo'.isupper())
>> False
print('MOOOO'.isupper())
>> True

# 1.8
# The join() method is rather complicated, so let us guide you step by step thorough it:
as its name suggests, the method performs a join - it expects one argument as a list; it must be assured that all the list's elements are strings - the method will raise a TypeError exception otherwise;
all the list's elements will be joined into one string but...
...the string from which the method has been invoked is used as a separator, put among the strings;
the newly created string is returned as a result.
  Let's analyze it:

the join() method is invoked from within a string containing a comma (the string can be arbitrarily long, or it can be empty)
the join's argument is a list containing three strings;
the method returns a new string.
# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))
>> omicron,pi,rho

# 1.9
# The lower() method
# The lower() method makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts, and returns the string as the result. Again, the source string remains untouched.
# Note: The lower() method doesn't take any parameters.
# Demonstrating the lower() method:
print("SiGmA=60".lower())
>> sigma=60

# 1.10
# The lstrip() method
# The parameterless lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.
# Analyze the example code in the editor.
# The brackets are not a part of the result - they only show the result's boundaries.
# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
>> [tau ]

# The one-parameter lstrip() method does the same as its parameterless version, but removes all characters enlisted in its argument (a string), not just whitespaces:

print("www.cisco.com".lstrip("w."))
>> cisco.com

print("pythoninstitute.org".lstrip(".org"))
>> pythoninstitute.org

# 1.11
# The replace() method
# The two-parameter replace() method returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
>> www.pythoninstitute.org
print("This is it!".replace("is", "are"))
>> Thare are it!
print("Apple juice".replace("juice", ""))
>> Apple 

# If the second argument is an empty string, replacing is actually removing the first argument's string. 
# The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.
print("This is it!".replace("is", "are", 1))
>> Thare is it!
print("This is it!".replace("is", "are", 2))
>> Thare are it!

# 1.12
# The rfind() method
# The one-, two-, and three-parameter methods named rfind() do nearly the same things as their counterparts (the ones devoid of the r prefix), but start their searches from the end of the string, not the beginning (hence the prefix r, for right).
# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
>> 8
print("tau tau tau".rfind("ta", 9))
>> -1
print("tau tau tau".rfind("ta", 3, 9))
>> 4

# 1.13
# The rstrip() method
# Two variants of the rstrip() method do nearly the same as lstrips, but affect the opposite side of the string.
# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
>> [ upsilon]
print("cisco.com".rstrip(".com"))
>> cis

# 1.14
# The split() method
# The split() method does what it says - it splits the string and builds a list of all detected substrings.
# The method assumes that the substrings are delimited by whitespaces - the spaces don't take part in the operation, and aren't copied into the resulting list.
# If the string is empty, the resulting list is empty too.
# Demonstrating the split() method:
print("phi       chi\npsi".split())
>> ['phi', 'chi', 'psi']
# Note: the reverse operation can be performed by the join() method.

# 1.15
# The startswith() method
# The startswith() method is a mirror reflection of endswith() - it checks if a given string starts with the specified substring.
# Demonstrating the startswith() method:
print("omega".startswith("meg"))
>> False
print("omega".startswith("om"))
>> True

# The strip() method
# The strip() method combines the effects caused by rstrip() and lstrip() - it makes a new string lacking all the leading and trailing whitespaces.
# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")
>> [aleph]

# 1.16
# The swapcase() method
# The swapcase() method makes a new string by swapping the case of all letters within the source string: lower-case characters become upper-case, and vice versa.
# All other characters remain untouched.
# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())
>> i KNOW THAT i KNOW NOTHING.

# The title() method
# The title() method performs a somewhat similar function - it changes every word's first letter to upper-case, turning all other ones to lower-case.
# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())
>> I Know That I Know Nothing. Part 1.

# The upper() method
# Last but not least, the upper() method makes a copy of the source string, replaces all lower-case letters with their upper-case counterparts, and returns the string as the result.
# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())
>> I KNOW THAT I KNOW NOTHING. PART 2.

# 1.17
#What is the expected output of the following code?

for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')
>> ABC123xyx

#What is the expected output of the following code?

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2[-2])
>> of

#What is the expected output of the following code?

the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list)
print(s)
>> Where*are*the*snows?

#What is the expected output of the following code?

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)
>> It is either hard or possible













