# 1.4 Properties
class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
example_object_3 = ExampleClass(2)
example_object_5 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)
>>
{'_ExampleClass__first': 1} 5
{'_ExampleClass__first': 2} 5
{'_ExampleClass__first': 2} 5

# 1.5
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)
>> 
{'__module__': '__main__', 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x7f63f0bc30e0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
{'__module__': '__main__', 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x7f63f0bc30e0>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
{}

# 1.6
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)
>>
1
 print(example_object.b)
AttributeError: 'ExampleClass' object has no attribute 'b'

# 1.7
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass

>>
1


# 1.8
class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
>> True
print(hasattr(ExampleClass, 'prop'))
>> False

# 1.9
#Which of the Python class properties are instance variables and which are class variables? Which of them are private?

class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False
>> population and victims are class variables, while length and __venomous are instance variables (the latter is also private).

#You're going to negate the __venomous property of the version_2 object, ignoring the fact that the property is private. How will you do this?

version_2 = Python()
>> version_2._Python__venomous = not version_2._Python__venomous

#Write an expression which checks if the version_2 object contains an instance property named constrictor (yes, constrictor!).
>> hasattr(version_2, 'constrictor')



