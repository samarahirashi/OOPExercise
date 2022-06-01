# Circle

from Shape import Shape


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
        return "Circle-- Color: "+self._color+", Filled: "+str(self._filled)+", Radius: "+str(self._radius)


if __name__ == '__main__':
    example = Circle()
    print(example.toString())