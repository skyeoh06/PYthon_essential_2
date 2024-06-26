#How to build a hierarchy of classes
#Building a hierarchy of classes isn't just art for art's sake.
#If you divide a problem among classes and decide which of them should be located at the top and which should be placed at the bottom of the hierarchy, 
#you have to carefully analyze the issue, but before we show you how to do it (and how not to do it), we want to highlight an interesting effect. 
#It's nothing extraordinary (it's just a consequence of the general rules presented earlier), but remembering it may be key to understanding how some codes work, and how the effect may be used to build a flexible set of classes.
#Take a look at the code in the editor. Let's analyze it:
#there are two classes, named One and Two, while Two is derived from One. Nothing special. However, one thing looks remarkable - the do_it() method.
#the do_it()method is defined twice: originally inside One and subsequently inside Two. The essence of the example lies in the fact that it is invoked just once - inside One.
#The question is - which of the two methods will be invoked by the last two lines of the code?
#The first invocation seems to be simple, and it is simple, actually - invoking doanything() from the object named one will obviously activate the first of the methods.
#The second invocation needs some attention. It's simple, too if you keep in mind how Python finds class components. The second invocation will launch do_it() in the form existing inside the Two class, 
#regardless of the fact that the invocation takes place within the One class.
class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
>> do_it from One
two.doanything()
>> do_it from Two


