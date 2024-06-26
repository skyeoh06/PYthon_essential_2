#The diamond problem
#The second example of the spectrum of issues that can possibly arise from multiple inheritance is illustrated by a classic problem named the diamond problem. 
#there is the top-most superclass named A;
#there are two subclasses derived from A: B and C;
#and there is also the bottom-most subclass named D, derived from B and C (or C and B, as these two variants mean different things in Python).
#Python, however, has chosen a different route – it allows multiple inheritance,
class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
>> bottom
object.m_middle()
>> middle_left
object.m_top()
>> top

#Note: both Middle classes define a method of the same name: m_middle().
#It introduces a small uncertainty to our sample, although we're absolutely sure that you can answer the following key question: which of the two m_middle() methods will actually be invoked when the following line is executed?

Object.m_middle()
#In other words, what will you see on the screen: middle_left or middle_right?
#You don't need to hurry – think twice and keep Python's MRO in mind!
#condition 1:
class Top:
    def m_top(self):
        print("top")

class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")

class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
>> bottom
object.m_middle()
>> middle_left
object.m_top()
>> top

#condition 2:
class Top:
    def m_top(self):
        print("top")

class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")

class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Bottom(Middle_Right,Middle_Left):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
>> bottom
object.m_middle()
>> middle_right
object.m_top()
>> top

#condition 3:
class Top:
    def m_top(self):
        print("top")

class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")
        
class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Right,Middle_Left):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
>> bottom
object.m_middle()
>> middle_right
object.m_top()
>> top

#condition 4:
class Top:
    def m_top(self):
        print("top")
    def m_middle(self):
        print("middle_top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
>> bottom
object.m_middle()
>> middle_left
object.m_top()
>> top
