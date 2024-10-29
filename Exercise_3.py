import math


class MyPoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'({self._x}, {self._y})'

    def distance(self, another = None, y = None):
        if another is None and y is None:
            return math.sqrt(self._x**2 + self._y**2)
        elif isinstance(another, MyPoint):
            dx = another._x - self._x
            dy = another._y - self._y
            return math.sqrt(dx**2 + dy**2)
        else:
            raise "Invalid arguments"

class MyTriangle:
    def __init__(self, x1 = None, y1 = None, x2 = None, y2 = None, x3 = None, y3 = None, v1 = None, v2 = None, v3 = None):
        if v1 is not None and v2 is not None and v3 is not None:
            self._v1 = v1
            self._v2 = v2
            self._v3 = v3
        elif x1 is not None and y2 is not None and x3 is not None and y3 is not None:
            self._v1 = MyPoint(x1, y1)
            self._v2 = MyPoint(x2, y2)
            self._v3 = MyPoint(x3, y3)

    def __str__(self):
        return f'MyTriangle=[({self._v1}, {self._v2}, {self._v3})]'

    def getPerimeter(self):
        side1 = self._v1.distance(self._v2)
        side2 = self._v2.distance(self._v3)
        side3 = self._v3.distance(self._v1)
        return side1 + side2 + side3

    def getType(self):
        side1 = self._v1.distance(self._v2)
        side2 = self._v2.distance(self._v3)
        side3 = self._v3.distance(self._v1)
        if side1 ==  side2 == side3:
            return "Equilateral"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "Isosceles"
        else:
            return "Scalene"

# Test MyTriangle's getType() method
ta1 = MyTriangle(1,1,3,3,4,-4)
p1 = MyPoint(0,0)
p2 = MyPoint(5,5)
p3 = MyPoint(10,0)
ta2 = MyTriangle(v1 = p1, v2 = p2, v3 = p3)
ta3 = MyTriangle(v1 = MyPoint(0,0), v2 = MyPoint(2,0), v3 = MyPoint(1,math.sqrt(3)))

print(ta1.getType())
print(ta2.getType())
print(ta3.getType())