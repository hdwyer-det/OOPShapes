# This file is to demonstrate solving problems similar to Task 1 using an OOP

import math

# This is the parent two dimensional shape class
class TwoDShape():
    def __init__(self):
        self.__area = None

    # This method will need to be overwritten on each child class
    # as the will have different formulas for calculating the area
    def __calculateArea(self):
        return None
    
    # This method will only be defined on the parent class
    def getArea(self):
        return self.__area


# This is the rectangle class
class Rectangle():

    # The initialisation method is called each time
    #  a new object is instantiated
    def __init__(self, rectLength, rectWidth):

        # Call the init method on the parent class
        super().__init__()

        self.__length = rectLength
        self.__width = rectWidth
        self.__area = self.__calculateArea()

    # This is an overwride of the calculateArea method
    def __calculateArea(self):
        return self.__length * self.__width

    def setLength(self, length):
        self.__length = length
        self.__area = self.calculateArea()

    def setWidth(self, width):
        self.__width = width
        self.__area = self.calculateArea()

    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width

# This is the triangle class
class Triangle():

    # The initialisation method is called each time
    #  a new object is instantiated
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = self.calculateArea()

    def __calculateArea(self):
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

    def __calculateArea(self):
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
