import math

from shapes.detect import is_rectangle, is_triangle


def rectangle_perimeter(rect_sides):
    if is_rectangle(rect_sides):
        return sum(rect_sides)
    else:
        print(f"Provided rectangle {rect_sides} is not a prober rectangle")


def rectangle_area(rect_sides):
    if is_rectangle(rect_sides):
        unique_sides = list(set(rect_sides))
        if len(unique_sides) == 1:
            # this is a square
            return unique_sides[0] ** 2
        else:
            # rectangle
            return unique_sides[0] * unique_sides[1]
    else:
        print(f"Provided rectangle {rect_sides} is not a prober rectangle")


def triangle_perimeter(tri_sides):
    if is_triangle(tri_sides):
        return sum(tri_sides)
    else:
        print(f"Provided triangle {tri_sides} is not a prober triangle")


def triangle_area(tri_sides):
    if is_triangle(tri_sides):
        s = sum(tri_sides) / 2
        return math.sqrt(s * (s-tri_sides[0]) *(s-tri_sides[1]) * (s-tri_sides[2]))
    else:
        print(f"Provided triangle {tri_sides} is not a prober triangle")