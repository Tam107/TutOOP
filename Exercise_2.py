import math


class MyPoint:

    def __init__(self, x = 0, y = 0) -> int:
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def getXY(self):
        return [self._x, self._y]

    def setXY(self, x,y):
        self._x = x
        self._y = y
        return self

    def __str__(self):
        return f'({self._x},{self._y})'

    def distance(self, another=None, y=None):
        if another is None and y is None:
            # Tính khoảng cách đến gốc tọa độ (0, 0)
            return math.sqrt(self._x ** 2 + self._y ** 2)
        elif isinstance(another, MyPoint):
            # Tính khoảng cách đến một điểm khác
            dx = self._x - another.getX()
            dy = self._y - another.getY()
            return math.sqrt(dx ** 2 + dy ** 2)
        elif isinstance(another, (int, float)) and isinstance(y, (int, float)):
            # Tính khoảng cách đến điểm có tọa độ (another, y)
            dx = self._x - another
            dy = self._y - y
            return math.sqrt(dx ** 2 + dy ** 2)
        else:
            raise ValueError("Invalid arguments for distance method")

class MyLine:
    def __init__(self, x1=None, y1=None, x2=None, y2=None, begin=None, end=None):
        if begin is not None and end is not None:
            self._begin = begin
            self._end = end
        elif x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            self._begin = MyPoint(x1, y1)
            self._end = MyPoint(x2, y2)
        else:
            raise ValueError("Invalid arguments for line method")

    def getBegin(self):
        return self._begin

    def getEnd(self):
        return self._end

    def setBegin(self, begin):
        self._begin = begin

    def setEnd(self, end):
        self._end = end

    def getBeginX(self):
        return self._begin.getX()

    def getBeginY(self):
        return self._begin.getY()

    def getEndX(self):
        return self._end.getX()

    def getEndY(self):
        return self._end.getY()

    def getBeginXY(self):
        return [self._begin.getX(), self._begin.getY()]

    def getEndXY(self):
        return [self._end.getX(), self._end.getY()]

    def setBeginX(self, x):
        self._begin.setX(x)

    def setBeginY(self, y):
        self._begin.setY(y)

    def setEndX(self, x):
        self._end.setX(x)

    def setEndY(self, y):
        self._end.setY(y)

    def setBeginXY(self, x, y):
        self._begin.setXY(x, y)

    def setEndXY(self, x, y):
        self._end.setXY(x, y)

    def getLength(self):
        return self._begin.distance(self._end)

    def getGradient(self):
        dx = self._begin.getX() - self._end.getX()  # Swap dx calculation
        dy = self._begin.getY() - self._end.getY()  # Swap dy calculation
        return math.atan2(dy, dx)

    def __str__(self):
        return f"MyLine[begin={self._begin}, end={self._end}]"


line1 = MyLine(1,2,7,8)
line2 = MyLine(10,10,20,30)

print(line1.getLength())
print(line2.getLength())
print(line1.getGradient())
print(line2.getGradient())
# # Test MyLine's setters
# line1 = MyLine(1,2,7,8)
#
# line1.setBegin(MyPoint(3,4))
# line1.setEnd(MyPoint(9,10))
# print(line1)
#
# line1.setBeginX(5)
# line1.setBeginY(6)
# line1.setEndX(11)
# line1.setEndY(12)
# print(line1)
#
# line1.setBeginXY(7,8)
# line1.setEndXY(13,14)
# print(line1)