# This file is to demonstrate solving problems similar to Task 1 using an OOP

import math

# This is the parent two dimensional shape class
class TwoDShape():
    def __init__(self):
        self.area = None

    # This method will need to be overwritten on each child class
    # as the will have different formulas for calculating the area
    def calculateArea(self):
        return None
    
    # This method will only be defined on the parent class
    def getArea(self):
        return self.area


# This is the rectangle class
class Rectangle(TwoDShape):

    # The initialisation method is called each time
    #  a new object is instantiated
    def __init__(self, rectLength, rectWidth):

        # Call the init method on the parent class
        super().__init__()

        self.length = rectLength
        self.width = rectWidth
        self.area = self.calculateArea()

    # This is an overwride of the calculateArea method
    def calculateArea(self):
        return self.length * self.width

    def setLength(self, length):
        self.length = length
        self.area = self.calculateArea()

    def setWidth(self, width):
        self.width = width
        self.area = self.calculateArea()


# This is the triangle class
class Triangle():

    # The initialisation method is called each time
    #  a new object is instantiated
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = self.calculateArea()

    def calculateArea(self):
        return 0.5 * self.base * self.height

    def setBase(self, base):
        self.base = base
        self.area = self.calculateArea()

    def setHeight(self, height):
        self.height = height
        self.area = self.calculateArea()

# This is the circle class
class Circle():

    # The initialisation method is called each time
    #  a new object is instantiated
    def __init__(self, radius):
        self.radius = radius
        self.area = self.calculateArea()

    def calculateArea(self):
        return math.pi * self.radius **2 

    def setRadius(self, radius):
        self.radius = radius




# The main program
rect1 = Rectangle(10, 3)
print(rect1.getArea())

rect2 = Rectangle(3, 5)
print(rect2.getArea())

# rect2.length = 100
# print(rect2.area)
# rect2.area = rect2.calculateArea()
# print(rect2.area)
rect2.setLength(100)
print(rect2.getArea())

tri1 = Triangle(10, 2)
print(f"Triangle area is: {tri1.getArea()}")

circ1 = Circle(5)
print(f"Circle area is {circ1.getArea()}")
