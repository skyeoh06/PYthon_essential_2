# 1.16
import time

class TrackedVehicle:
    def control_track(left, stop):
        pass

    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)


class WheeledVehicle:
    def turn_front_wheels(left, on):
        pass

    def turn(left):
        turn_front_wheels(left, True)
        time.sleep(0.25)
        turn_front_wheels(left, False)


# 1.17
#we defined a superclass named Vehicle, which uses the turn() method to implement a general scheme of turning, while the turning itself is done by a method named change_direction(); note: the former method is empty, 
#as we are going to put all the details into the subclass (such a method is often called an abstract method, as it only demonstrates some possibility which will be instantiated later)
#we defined a subclass named TrackedVehicle (note: it's derived from the Vehicle class) which instantiated the change_direction() method by using the specific (concrete) method named control_track()
#respectively, the subclass named WheeledVehicle does the same trick, but uses the turn_front_wheels() method to force the vehicle to turn.
#The most important advantage (omitting readability issues) is that this form of code enables you to implement a brand new turning algorithm just by modifying the turn() method, which can be done in just one place, 
#as all the vehicles will obey it.
#This is how polymorphism helps the developer to keep the code clean and consistent.
import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)
