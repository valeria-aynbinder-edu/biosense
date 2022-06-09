def is_valid_side(side):
    return (type(side) == int or type(side) == float) and float(side) > 0


def is_numeric_positive_sides(sides):
    for side in sides:
        if not is_valid_side(side):
            return False
    return True

def is_proper_triangle(sides):
    return sides[0] + sides[1] > sides[2] and \
        sides[1] + sides[2] > sides[0] and \
        sides[0] + sides[2] > sides[1]


def is_rectangle(sides:list) -> bool:
    # check all positive numbers
    return len(sides) == 4 and is_numeric_positive_sides(sides) and len(set(sides)) in (1,2)


def is_square(sides):
    return len(sides) == 4 and is_numeric_positive_sides(sides) and len(set(sides)) == 1


def is_triangle(sides):
    return len(sides) == 3 and is_numeric_positive_sides(sides) and is_proper_triangle(sides)

