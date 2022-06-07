from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


class Triangle(Shape):

    def __init__(self, side1, side2, side3):
        self.sides = (side1, side2, side3)

    def area(self):
        s = sum(self.sides) / 2
        return sqrt(s * (s-self.sides[0]) * (s-self.sides[1]) * (s-self.sides[2]))

    # def perimeter(self):
    #     return sum(self.sides)


if __name__ == '__main__':

    t1 = Triangle(3,4,5)
    print(f"{t1.area()}")

    s = Shape()
    print(s.area())