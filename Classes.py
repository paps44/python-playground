# Classes are extremely important in programming & they are not specific to python
# Other programming languages do support the notion of classes.
# We use classes to define new types
# Simple classes in Python include Numbers, Strings Booleans & complex types like Lists and Dictionaries.

#we start by defining a class giving our class a name, the name after class is capital
#letter using the Pascal naming convention. The convention we use in naming our classes is
#different from the convention use in our variables & functions. For variable and f! we
#use lower case letters and we separate multiple words using and underscore

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

