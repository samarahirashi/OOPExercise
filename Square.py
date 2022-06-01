# Square

from Rectangle import Rectangle


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
        return "Square-- Color: "+self._color+", Filled: "+str(self._filled)+", Width: "+str(self._width)+", Length: "+str(self._length)


if __name__ == '__main__':
    example = Square()
    print(example.toString())
