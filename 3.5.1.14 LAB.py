#Let's take a look at the example in the editor.
#The Sub class inherits goods from two superclasses, Left and Right (these names are intended to be meaningful).
#There is no doubt that the class variable var_right comes from the Right class, and var_left comes from Left respectively.
#This is clear. But where does var come from? Is it possible to guess it? The same problem is encountered with the fun() method - will it be invoked from Left or from Right? Let's run the program - its output is:
#L LL RR Left
#This proves that both unclear cases have a solution inside the Left class. Is this a sufficient premise to formulate a general rule? Yes, it is.
#We can say that Python looks for object components in the following order:
#inside the object itself;
#in its superclasses, from bottom to top;
#if there is more than one class on a particular inheritance path, Python scans them from left to right.
#Do you need anything more? Just make a small amendment in the code - replace: class Sub(Left, Right): with: class Sub(Right, Left):, then run the program again, and see what happens.
class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())
>> L LL RR Left
