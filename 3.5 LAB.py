# 1.1
# Inheritance 
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


sun = Star("Sun", "Milky Way")
venus =Star("Venus","orbit")
print(sun)
>> <__main__.Star object at 0x7f36d97f8410>
print(venus)
>> <__main__.Star object at 0x7f36d97f8490>

# 1.2
# When Python needs any class/object to be presented as a string (putting an object as an argument in the print() function invocation fits this condition) 
# it tries to invoke a method named __str__() from the object and to use the string it returns.

# The default __str__() method returns the previous string - ugly and not very informative. You can change it just by defining your own method of the name.
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy


sun = Star("Sun", "Milky Way")
venus =Star("Venus","orbit")
print(sun)
>> Sun in Milky Way
print(venus)
>> Venus in orbit

# 1.4
# issubclass(ClassOne, ClassTwo)
# issubclass(ClassOne, ClassTwo)
# The function returns True if ClassOne is a subclass of ClassTwo, and False otherwise.
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()
>>
True	False	False	
True	True	False	
True	True	True
# ↓ is a subclass of →	Vehicle	LandVehicle	TrackedVehicle
# Vehicle	              True	  False	      False
# LandVehicle	          True	  True	      False
# TrackedVehicle	      True	  True	      True
# There is one important observation to make: each class is considered to be a subclass of itself.


# 1.5
# Similarly, it can be crucial if the object does have (or doesn't have) certain characteristics. In other words, whether it is an object of a certain class or not.
# Such a fact could be detected by the function named isinstance():

# isinstance(objectName, ClassName)

# The functions returns True if the object is an instance of the class, or False otherwise.
# Being an instance of a class means that the object (the cake) has been prepared using a recipe contained in either the class or one of its superclasses.
# Don't forget: if a subclass contains at least the same equipment as any of its superclasses, it means that objects of the subclass can do the same as objects derived from the superclass, ergo, 
# it's an instance of its home class and any of its superclasses.
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()

>>
True	False	False	
True	True	False	
True	True	True	

# Let's make the result more readable once again:

# ↓ is an instance of →	Vehicle	LandVehicle	TrackedVehicle
# my_vehicle	          True	    False	    False
# my_land_vehicle	      True	    True	    False
# my_tracked_vehicle	   True	    True	    True

# 1.6
# Inheritance: the is operator
# There is also a Python operator worth mentioning, as it refers directly to objects - here it is:
# object_one is object_two
# The is operator checks whether two variables (object_one and object_two here) refer to the same object.
# Don't forget that variables don't store the objects themselves, but only the handles pointing to the internal Python memory.
# Assigning a value of an object variable to another variable doesn't copy the object, but only its handle. This is why an operator like is may be very useful in particular circumstances.
# Take a look at the code in the editor. Let's analyze it:
# there is a very simple class equipped with a simple constructor, creating just one property. The class is used to instantiate two objects. The former is then assigned to another variable, and its val property is incremented by one.
# afterward, the is operator is applied three times to check all possible pairs of objects, and all val property values are also printed.
# the last part of the code carries out another experiment. After three assignments, both strings contain the same texts, but these texts are stored in different objects.
class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
>> False
print(object_2 is object_3)
>> False
print(object_3 is object_1)
>> True
print(object_1.val, object_2.val, object_3.val)
>> 1 2 1

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)
>> True False

# 1.7
# How Python finds properties and methods
# Now we're going to look at how Python deals with inheriting methods.
# Take a look at the example in the editor. Let's analyze it:
# there is a class named Super, which defines its own constructor used to assign the object's property, named name.
# the class defines the __str__() method, too, which makes the class able to present its identity in clear text form.
# the class is next used as a base to create a subclass named Sub. The Sub class defines its own constructor, which invokes the one from the superclass. Note how we've done it: Super.__init__(self, name).
# we've explicitly named the superclass, and pointed to the method to invoke __init__(), providing all needed arguments.
# we've instantiated one object of class Sub and printed it.
# Note: As there is no __str__() method within the Sub class, the printed string is to be produced within the Super class. This means that the __str__() method has been inherited by the Sub class.

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)
>> My name is Andy.

# 1.8
# The super() function creates a context in which you don't have to (moreover, you mustn't) pass the self argument to the method being invoked - 
# this is why it's possible to activate the superclass constructor using only one argument.
# Note: you can use this mechanism not only to invoke the superclass constructor, but also to get access to any of the resources available inside the superclass.

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Merci")

print(obj)
>> My name is Merci.

# 1.9
# As you can see, the Super class defines one class variable named supVar, and the Sub class defines a variable named subVar.
# Both these variables are visible inside the object of class Sub.
# Testing properties: class variables.
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
>> 2
print(obj.supVar)
>> 1

# 1.10
# The same effect can be observed with instance variables - take a look at the second example in the editor.
# The Sub class constructor creates an instance variable named subVar, while the Super constructor does the same with a variable named supVar. 
# As previously, both variables are accessible from within the object of class Sub.
# Note: the existence of the supVar variable is obviously conditioned by the Super class constructor invocation. Omitting it would result in the absence of the variable in the created object.
# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
>> 12
print(obj.supVar)
>> 11

# 1.11
# When you try to access any object's entity, Python will try to (in this order):
# find it inside the object itself;
# find it in all classes involved in the object's inheritance line from bottom to top;
# If both of the above fail, an exception (AttributeError) is raised.
# The first condition may need some additional attention. As you know, all objects deriving from a particular class may have different sets of attributes,
# and some of the attributes may be added to the object a long time after the object's creation.
# The example in the editor summarizes this in a three-level inheritance line. Analyze it carefully.
# All the comments we've made so far are related to single inheritance, when a subclass has exactly one superclass. This is the most common situation (and the recommended one, too).
class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
>> 100 101 102
print(obj.variable_2, obj.var_2, obj.fun_2())
>> 200 201 202
print(obj.variable_3, obj.var_3, obj.fun_3())
>> 300 301 302

# 1.12
# Multiple inheritance occurs when a class has more than one superclass. Syntactically, such inheritance is presented 
# as a comma-separated list of superclasses put inside parentheses after the new class name - just like here:
class SuperA:
    var_a = 10
    def fun_a(self):
        return 11


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, obj.fun_a())
>> 10 11
print(obj.var_b, obj.fun_b())
>> 20 21
# The Sub class has two superclasses: SuperA and SuperB. This means that the Sub class inherits all the goods offered by both SuperA and SuperB.
