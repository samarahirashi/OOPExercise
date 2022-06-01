# Shape
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

