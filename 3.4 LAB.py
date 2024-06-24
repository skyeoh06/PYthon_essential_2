# 1.1
class Classy:
    def method(self):
        print("method")


obj = Classy()
obj.method()
>> method

# 1.2
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()
>> 2 3

class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()
>>
method
other

# 1.3
class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("object")

print(obj_1.var)
>> object

# 1.4
class Classy:
    def __init__(self, value = None):
        self.var = value


obj_1 = Classy("object")
obj_2 = Classy()

print(obj_1.var)
>> object

print(obj_2.var)
>> None

class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()
>> visible


try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()
>>
failed
hidden

# 1.5
class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
>> {'var': 2}
print(Classy.__dict__)
>> {'__module__': '__main__', 'varia': 1, '__init__': <function Classy.__init__ at 0x7fb0253c8320>, 'method': <function Classy.method at 0x7fb0253c83b0>, '_Classy__hidden': <function Classy.__hidden at 0x7fb0253c8440>, '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>, '__doc__': None}

# 1.6
class Classy:
    pass


print(Classy.__name__)
>> Classy
obj = Classy()
print(type(obj).__name__)
>> Classy

# 1.7
class Classy:
    pass


print(Classy.__module__)
>> __main__
obj = Classy()
print(obj.__module__)
>> __main__

# 1.8
class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
>> ( object )
printBases(SuperTwo)
>> ( object )
printBases(Sub)
>> ( SuperOne SuperTwo )

# 1.10
class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
>> {'a': 1, 'b': 2, 'i': 3, 'ireal': 3.5, 'integer': 4, 'z': 5}
incIntsI(obj)
print(obj.__dict__)
>> {'a': 1, 'b': 2, 'i': 4, 'ireal': 3.5, 'integer': 5, 'z': 5}

# 1.11
#The declaration of the Snake class is given below. Enrich the class with a method named increment(), adding 1 to the victims property.

class Snake:
    def __init__(self):
        self.victims = 0

>> def increment(self):
        self.victims += 1

#Redefine the Snake class constructor so that is has a parameter to initialize the victims field with a value passed to the object during construction.
>>
class Snake:
    def __init__(self, victims):
        self.victims = victims	

#Can you predict the output of the following code?

class Snake:
    pass


class Python(Snake):
    pass


print(Python.__name__, 'is a', Snake.__name__)
print(Python.__bases__[0].__name__, 'can be a', Python.__name__)
>>
Python is a Snake
Snake can be a Python


