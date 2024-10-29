import math

class Circle:
    def __init__(self, radius=1.0, color="red"):
        self.__radius = radius
        self.__color = color

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def setRadius(self, radius):
        self.__radius = radius

    def setColor(self, color):
        self.__color = color

    def getArea(self):
        return math.pi * self.__radius * self.__radius

    def __str__(self):
        return f"Circle[radius = {self.__radius}, color = {self.__color}]"


class Cylinder(Circle):
    def __init__(self, radius=1.0, height=1.0, color="red"):
        super().__init__(radius, color)
        self._height = height

    def getHeight(self):
        return self._height

    def setHeight(self, height):
        self._height = height

    def getArea(self):
        surfaceArea = 2 * math.pi * self.getRadius() * self.getHeight() + Circle.getArea(self)
        return surfaceArea

    def getVolume(self):
        return Circle.getArea(self)  * self._height  # Correct usage

    def __str__(self):
        return f"Cylinder[radius:{self.getRadius()}, height:{self._height}, color:{self.getColor()}]"

# Test Cylinder's getVolume() method
cy1 = Cylinder(4.0, 8.0, "blue")
cy2 = Cylinder(5.5, 9.5,"green")
print(cy1.getVolume())
print(cy2.getVolume())