import pprint

from shapes.complex import analyse_shapes

if __name__ == '__main__':
    shapes = []
    while True:
        user_choice = input(f"Enter i to insert a shape, q to quit")
        if user_choice == 'q':
            pprint.pprint(analyse_shapes(shapes))
            exit()
        elif user_choice == 'i':
            sides = input("Insert shape represented by side lengths, separated by comma")
            shapes.append([float(side) for side in sides.split(",")])
        else:
            print("Wrong input")