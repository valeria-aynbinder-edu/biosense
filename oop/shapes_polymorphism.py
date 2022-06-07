from math import sqrt


class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


class Triangle:

    def __init__(self, side1, side2, side3):
        self.sides = (side1, side2, side3)

    def area(self):
        s = sum(self.sides) / 2
        return sqrt(s * (s-self.sides[0]) * (s-self.sides[1]) * (s))

    def perimeter(self):
        return sum(self.sides)