# This file is to demonstrate solving problems similar to Task 1 using an OOP

# This is the rectangle class
class Rectangle():

    # The initialisation method is called each time
    #  a new object is instantiated
    def __init__(self, rectLength, rectWidth):
        self.length = rectLength
        self.width = rectWidth
        self.area = self.calculateArea()

    def calculateArea(self):
        return self.length * self.width

    def setLength(self, length):
        self.length = length
        self.area = self.calculateArea()


# The main program
rect1 = Rectangle(10, 3)
print(rect1.area)

rect2 = Rectangle(3, 5)
print(rect2.area)

# rect2.length = 100
# print(rect2.area)
# rect2.area = rect2.calculateArea()
# print(rect2.area)
rect2.setLength(100)
print(rect2.area)
