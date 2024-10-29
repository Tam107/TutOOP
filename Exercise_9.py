import math


class Shape:
    def __init__(self, color = "red", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return f"Shape[color={self.getColor()},filled={self.isFilled()}]"

class Circle(Shape):

    def __init__(self, radius = 1.0, color = "red", filled = True):
        super().__init__(color, filled)
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return (self.__radius * self.__radius) * math.pi

    def getPerimeter(self):
        return 2 * math.pi* self.__radius

    def __str__(self):
        return f"Circle[{Shape.__str__(self)},radius={self.getRadius()}]"

class Rectangle(Shape):
    def __init__(self, width = 1.0, length = 1.0, color = "red", filled = True):
        super().__init__(color, filled)
        self.__width = width
        self.__length = length

    def getWidth(self):
        return self.__width

    def setSide(self, side):
        self.__side = side

    def setWidth(self, width):
        self.__width = width

    def getLength(self):
        return self.__length

    def setLength(self, length):
        self.__length = length

    def getArea(self):
        return self.__length * self.__width

    def getPerimeter(self):
        return 2 * (self.__length + self.__width)

    def __str__(self):
        return f"Rectangle[{Shape.__str__(self)},width={self.__width},length={self.__length}]"

class Square(Rectangle):
    def __init__(self, side=1.0, color="red", filled=True):
        super().__init__(side, side, color, filled)  # Initialize Rectangle with equal width and length
        self.__side = side

    def getSide(self):
        return self.__side

    def setSide(self, side):
        self.__side = side
        self.setWidth(side)  # Ensure width and length remain equal
        self.setLength(side)

    def setWidth(self, width):
        self.__side = width
        super().setWidth(width)
        super().setLength(width)

    def setLength(self, length):
        self.__side = length
        super().setWidth(length)
        super().setLength(length)

    def __str__(self):
        return f"Square[{super().__str__()}]"

# sq1 = Square()
# print(sq1)a
# sq2 = Square(side = 3.0)
# print(sq2)
# sq3 = Square(5.5, "white", False)
# print(sq3)