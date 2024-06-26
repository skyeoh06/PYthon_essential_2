# 1.13
# Assuming that there is a class named Snakes, write the very first line of the Python class declaration, expressing the fact that the new class is actually a subclass of Snake.
>> class Python(Snakes):

#Something is missing from the following declaration – what?

class Snakes:
    def __init__():
        self.sound = 'Sssssss'
>> The __init__() constructor lacks the obligatory parameter (we should name it self to stay compliant with the standards).

#Modify the code to guarantee that the venomous property is private.

class Snakes:
    def __init__(self):
        self.venomous = True

>> class Snakes:
    def __init__(self):
        self.__venomous = True
