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

    def getVolume(self):
        return self.getArea() * self._height  # Correct usage

    def __str__(self):
        return f"Cylinder[radius={self.getRadius()}, color={self.getColor()}, height={self._height}]"
