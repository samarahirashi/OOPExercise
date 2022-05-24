# OOP
import math
from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, color="Red", filled=True):
        self._color = color
        self._filled = filled

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
        return "Color: "+self._color+", Filled: "+str(self._filled)


class Circle(Shape):

    _radius = 1.0

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
        return "Color: "+self._color+", Filled: "+str(self._filled)+", Radius: "+str(self._radius)


class Rectangle(Shape):

    _width = 1.0
    _length = 1.0

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
        return "Color: "+self._color+", Filled: "+str(self._filled)+", Width: "+str(self._width)+", Length: "+str(self._length)


class Square(Rectangle):

    side = 0

    def getSide(self):
        return self.side

    def setSide(self, value):
        self.side = value

    def setWidth(self, value):
        self._width = value

    def setLength(self, value):
        self._length = value

    def toString(self):
        return "Color: "+self._color+", Filled: "+str(self._filled)+", Width: "+str(self._width)+", Length: "+str(self._length)


class EquilateralTriangle(Shape):

    _sideLength = 1.0

    def getSideLength(self):
        return self._sideLength

    def setSideLength(self, value):
        self._sideLength = value

    def getArea(self):
        area = (math.sqrt(3)/4)*(self._sideLength*self._sideLength)
        return area

    def getPerimeter(self):
        result = self._sideLength * 3
        return result

    def toString(self):
        return "Color: "+self._color+", Filled: "+str(self._filled)+", Side Length:"+str(self._sideLength)


if __name__ == '__main__':
    example = Circle()
    print(example.toString())
