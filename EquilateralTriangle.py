# Equilateral Triangle

from Shape import Shape
import math


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
        return "Equilateral Triangle-- Color: "+self._color+", Filled: "+str(self._filled)+", Side Length:"+str(self._sideLength)


if __name__ == '__main__':
    example = EquilateralTriangle()
    print(example.toString())