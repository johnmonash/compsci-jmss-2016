#OO practice. Some parts shamelessly lifted from "How to think like a Computer Scientist" (ThinkPython)

#TODO - allow for initialising the point with a set of co-ords
#TODO - method to determine distance from origin
#TODO - create method to allow you to `print Point()` and have meaningful output
#TODO - allow to check if two points are equal using ==
#TODO - method `distance_from_point` to determine distance to another point
#TODO - method `move(dx, dy)` to move the given point by a set amount
#TODO - method to convert to polar co-ordinates
#TODO - allow for addition, subtraction and multiplication
#TODO - draw points (ASCII? canvas?)
#TODO - implement lines

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p)
print(q)


print(p is q)