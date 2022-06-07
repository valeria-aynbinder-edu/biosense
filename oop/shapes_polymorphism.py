from math import sqrt


class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        print("Calling area on rectangle")
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return f"Rectangle with height {self.height} and width {self.width}"


class Triangle:

    def __init__(self, side1, side2, side3):
        self.sides = (side1, side2, side3)

    def area(self):
        print("Calling area on triangle")
        s = sum(self.sides) / 2
        return sqrt(s * (s-self.sides[0]) * (s-self.sides[1]) * (s))

    def perimeter(self):
        return sum(self.sides)

    def __add__(self, other):
        if type(other) == int:
            new_tri = Triangle(*(s+ other for s in self.sides))
            return new_tri


    def __str__(self):
        return f"Triangle with sides: {self.sides}"


if __name__ == '__main__':

    rec = Rectangle(5, 7)
    tri = Triangle(3, 4, 5)

    # print(f"Rectangle area: {rec.area()}")
    # print(f"Triangle area: {tri.area()}")

    figures_list = [rec, tri, Rectangle(9,19), Triangle(5,6,7), Triangle(15,8,9)]

    # for figure in figures_list:
    #     print(f"Area: {figure.area()}")

    print(tri + 5)