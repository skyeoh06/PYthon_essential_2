#Both, Level1 and Level2 classes define a method named fun() and a property named var. Does this mean that the Level3 class object will be able to access two copies of each entity? Not at all.
#The entity defined later (in the inheritance sense) overrides the same entity defined earlier. This is why the code produces the following output:
#200 201
#As you can see, the var class variable and fun() method from the Level2 class override the entities of the same names derived from the Level1 class.
#This feature can be intentionally used to modify default (or previously defined) class behaviors when any of its classes needs to act in a different way to its ancestor.
#We can also say that Python looks for an entity from bottom to top, and is fully satisfied with the first entity of the desired name.
class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())
>> 200 201
