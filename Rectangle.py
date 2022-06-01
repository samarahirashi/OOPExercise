# Rectangle

from Shape import Shape


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
        return "Rectangle-- Color: "+self._color+", Filled: "+str(self._filled)+", Width: "+str(self._width)+", Length: "+str(self._length)


if __name__ == '__main__':
    example = Rectangle()
    print(example.toString())
