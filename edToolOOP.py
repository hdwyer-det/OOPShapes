# This file is to demonstrate solving problems similar to Task 1 using an OOP

import math

# This is the parent two dimensional shape class
class TwoDShape():
    def __init__(self):
        self._area = None

    # This method will need to be overwritten on each child class
    # as the will have different formulas for calculating the area
    def _calculateArea(self):
        return None
    
    # This method will only be defined on the parent class
    def getArea(self):
        return self._area


# This is the rectangle class
class Rectangle(TwoDShape):

    # The initialisation method is called each time
    #  a new object is instantiated
    def __init__(self, rectLength, rectWidth):

        # Call the init method on the parent class
        super().__init__()

        self._length = rectLength
        self._width = rectWidth
        self._area = self._calculateArea()

    # This is an overwride of the calculateArea method
    def _calculateArea(self):
        return self._length * self._width

    def setLength(self, length):
        self._length = length
        self._area = self._calculateArea()

    def setWidth(self, width):
        self._width = width
        self._area = self._calculateArea()

    def getLength(self):
        return self._length
    
    def getWidth(self):
        return self._width

# This is the triangle class
class Triangle(TwoDShape):

    # The initialisation method is called each time
    #  a new object is instantiated
    def __init__(self, base, height):
        self._base = base
        self._height = height
        self._area = self._calculateArea()

    def _calculateArea(self):
        return 0.5 * self._base * self._height

    def setBase(self, base):
        self._base = base
        self._area = self._calculateArea()

    def setHeight(self, height):
        self._height = height
        self._area = self._calculateArea()

# This is the circle class
class Circle(TwoDShape):

    # The initialisation method is called each time
    #  a new object is instantiated
    def __init__(self, radius):
        self._radius = radius
        self._area = self._calculateArea()

    def _calculateArea(self):
        return math.pi * self._radius **2 

    def setRadius(self, radius):
        self._radius = radius
        self._area = self._calculateArea()




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

print("\n")

# Calculate area loop
command = -1
while command != 0:
    print("\nEnter shape type to calculate area")
    print("  1: for rectangle")
    print("  2: for triangle")
    print("  3: for circle")
    print("  0: to quit")

    command = int(input("Enter command: "))
    print("")

    # Create an object of the correct class
    if command == 1:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the length of the rectangle: "))
        shape = Rectangle(length, width)
    elif command == 2:
        base = int(input("Enter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        shape = Triangle(base, height)
    elif command == 3:
        radius = int(input("Enter the radius of the circle: "))
        shape = Circle(radius)

    # print the area of the shape
    print(f"The area of the shape is {shape.getArea()}")
