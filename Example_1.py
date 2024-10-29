import math

class Circle:
    def __init__(self, radius = 1.0, color = "red"):
        self._radius = radius
        self._color = color

    def getRadius(self):
        return self._radius

    def getColor(self):
        return self._color

    def setRadius(self, radius):
        self._radius = radius

    def setColor(self, color):
        self._color = color

    def getArea(self):
        return math.pi * self._radius ** 2

    def __str__(self):
        return f"Circle[radius = {self._radius}, color = {self._color}]"

c2 = Circle(2.0,"blue")
print(c2)
print(f"Circle area: {c2.getArea()}")