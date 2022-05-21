# OOP

from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self,color,filled):
        self._color = "Red"
        self._filled = True

    def getColor(self):
        return self._color

    def setColor(self, newcolor):
        self._color = newcolor

    def isFilled(self):
        return self._filled

    def setFilled(self, value):
        self._filled = value

    @abstractmethod
    def getArea(self):
        ...

    @abstractmethod
    def getPerimeter(self):
        ...

    def toString(self):
        return self._color, self._filled


class Circle(Shape):

    def __init__(self, radius):
        self._radius = 1.0

    def getRadius(self):
        return self._radius

    def setRadius(self, value):
        self._radius = value

    def getArea(self):
        pi = 3.14
        r = self._radius
        area = pi*r*r
        return area

    def getPerimeter(self):
        pi = 3.14
        r = self._radius
        perimeter = 2*pi*r
        return perimeter

    def toString(self):
        return self._color, self._filled, self._radius


class Rectangle(Shape):

    def __init__(self, width, length):
        self._width = 1.0
        self._length = 1.0

    def getWidth(self):
        return self._width

    def setWidth(self, value):
        self._width = value

    def getLength(self):
        return self._length

    def setLength(self, value):
        self._length = value

    def getArea(self):
        w = self._width
        l = self._length
        area = w*l
        return area

    def getPerimeter(self):
        w = self._width
        l = self._length
        perimeter = (w*2)+(l*2)
        return perimeter

    def toString(self):
        return self._color, self._filled, self._width, self._length


class Square(Rectangle):

    def __init__(self, side):
        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, value):
        self.side = value

    def setWidth(self, value):
        self._width = value

    def setLength(self, value):
        self._length = value

    def toString(self):
        return self._color, self._filled, self._width, self._length


if __name__ == '__main__':
    pass