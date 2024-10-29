import math


class MyPoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'({self._x},{self._y})'

    def distance(self, another = None, y = None):
        if another is None and y is None:
            return math.sqrt(self._x**2 + self._y**2)
        elif isinstance(another, MyPoint):
            dx = another._x - self._x
            dy = another._y - self._y
            return math.sqrt(dx**2 + dy**2)
        else:
            raise "Invalid arguments"

class MyPolyLine:

    def __init__(self, points = None):
        if points is None:
            self._points = []
        else:
            self._points = points


    def __str__(self):
        return "MyPolyLine{"+"".join(str(point) for point in self._points)+ "}"

    def appendPoint(self, x = None, y= None, point = None):
        if point is not None:
            self._points.append(point)
        elif x is not None and y is not None:
            self._points.append(MyPoint(x, y))


    def getLength(self):
        if len(self._points) < 2:
            return 0.0
        length = 0.0
        for i in range(1, len(self._points)):
            length += self._points[i-1].distance(self._points[i])
        return length

# Test MyPolyLine's appendPoint() method
# pl1 = MyPolyLine()
# pl1.appendPoint(2,3)
# pl1.appendPoint(point = MyPoint(4,4))
# print(pl1)
