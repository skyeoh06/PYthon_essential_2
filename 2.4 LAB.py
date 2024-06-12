# 1.1
# Comparing strings
print('alpha' == 'alpha')
>> True
print('alpha' != 'Alpha')
>> True
print('alpha' < 'alphabet')
>> True
print('beta' > 'Beta')
>> True

# 1.2
print('10' == '010')
>> False
print('10' > '010')
>> True
print('10' > '8')
>> False
print('20' < '8')]
>> True
print('20' < '80')
>> True
# Comparing strings against numbers
print('10' == 10)
>> False
print('10' != 10)
>> True
print('10' == 1)
>> False
print('10' != 1)
>> True
print('10' > 10)
>> TypeError: '>' not supported between instances of 'str' and 'int'

# 1.3
# Sorting
# The first is implemented as a function named sorted().
# The function takes one argument (a list) and returns a new list, filled with the sorted argument's elements. 
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
>> ['omega', 'alpha', 'pi', 'gamma']
print(first_greek_2)
>> ['alpha', 'gamma', 'omega', 'pi']

#The second method affects the list itself - no new list is created. Ordering is performed in situ by the method named sort().
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)
>> ['omega', 'alpha', 'pi', 'gamma']

second_greek.sort()
print(second_greek)
>>  
 Sandbox
Code
# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)
# first_greek = ['omega', 'alpha', 'pi', 'gamma']
# first_greek_2 = sorted(first_greek)


Console 
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']

['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']

# 1.4
# Strings vs. numbers
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)
>> 13 1.3

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)
>> 14.3

# 1.5
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])
>> are

s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)
>> ValueError: invalid literal for int() with base 10: '12.8'
