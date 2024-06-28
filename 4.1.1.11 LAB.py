#Lambdas and the map() function
#In the simplest of all possible cases, the map() function:

#map(function, list)
#takes two arguments:

#a function;
#a list.
#The above description is extremely simplified, as:

#the second map() argument may be any entity that can be iterated (e.g., a tuple, or just a generator)
#map() can accept more than two arguments.
#The map() function applies the function passed by its first argument to all its second argument's elements, and returns an iterator delivering all subsequent function results.
#You can use the resulting iterator in a loop, or convert it into a list using the list() function.
#This is the intrigue:

#build the list_1 with values from 0 to 4;
#next, use map along with the first lambda to create a new list in which all elements have been evaluated as 2 raised to the power taken from the corresponding element from list_1;
#list_2 is printed then;
#in the next step, use the map() function again to make use of the generator it returns and to directly print all the values it delivers;
#he second lambda here - it just squares each element from list_2.
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)


for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
>> [1, 2, 4, 8, 16]
1 4 16 64 256 
