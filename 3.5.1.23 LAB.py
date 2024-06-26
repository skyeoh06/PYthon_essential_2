#Scenario

#Assume that the following piece of code has been successfully executed:

class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: Woof!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister Intruder!"


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")


#What is the expected output of the following piece of code?

print(rocky)
>> Collie says: Woof! Don't run away, Little Lamb!
print(luna)
>> Dobermann says: Woof! Stay where you are, Mister Intruder!

#What is the expected output of the following piece of code?

print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
>> True, False
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))
>> False, True

#What is the expected output of the following piece of code?

print(luna is luna, rocky is luna)
>> True, False
print(rocky.kennel)
>> 2

#Define a SheepDog's subclass named LowlandDog, and equip it with an __str__() method overriding an inherited method of the same name. 
#The new dog's __str__() method should return the string "Woof! I don't like mountains!" .

>>
class LowlandDog(SheepDog):
    def __str__(self):
        return Dog.__str__(self) + " I don't like mountains!"
