from shapes.detect import *
from shapes.calc import *


def analyse_shapes(shapes):
    ret_dict = {}
    improper_shapes = []

    for shape in shapes:
        if is_square(shape):
            if 'squares' not in ret_dict:
                ret_dict['squares'] = []
            ret_dict['squares'].append({
                'sides': shape,
                'area': rectangle_area(shape),
                'perimeter': rectangle_perimeter(shape)
            })
        elif is_rectangle(shape):
            if 'rectangles' not in ret_dict:
                ret_dict['rectangles'] = []
            ret_dict['rectangles'].append({
                'sides': shape,
                'area': rectangle_area(shape),
                'perimeter': rectangle_perimeter(shape)
            })
        elif is_triangle(shape):
            if 'triangles' not in ret_dict:
                ret_dict['triangles'] = []
            ret_dict['triangles'].append({
                'sides': shape,
                'area': triangle_area(shape),
                'perimeter': triangle_perimeter(shape)
            })
        else:
            improper_shapes.append(shape)

    return ret_dict, improper_shapes
