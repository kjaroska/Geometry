import sys
from geometry import *

menu_options = """
Learn Geometry.
    What do you want to do?
    (1) Add new shape
    (2) Show all shapes
    (3) Show shape with the largest perimeter
    (4) Show shape with the largest area
    (5) Show formulas
    (0) Exit program"""

show_formula = """
Which formula do you need?
    (1) Circle
    (2) Triangle
    (3) Rectangle
    (4) Square
    (5) Regular Pentagon
    (0) Back to main menu
    >>>"""


def new_circle(shapes):
    '''Function that instantiates a circle object.'''
    r = int(input("Enter circle radius length >"))
    circle = Circle(r)
    shapes.add_shape(circle)


def new_triangle(shapes):
    '''Function that instantiates a triangle object.'''
    a = int(input("Enter first side's length >"))
    b = int(input("Enter second side's length >"))
    c = int(input("Enter third side's length >"))
    if a == b == c:
        print("Yay, your triangle is an Equilateral triangle!")
        triangle = EquilateralTriangle(a)
    else:
        triangle = Triangle(a, b, c)
    shapes.add_shape(triangle)


def new_rectangle(shapes):
    '''Function that instantiates a rectangle object.'''
    a = int(input ("Enter first side's length >"))
    b = int(input("Enter second side's length >"))
    if a == b:
        rectangle = Square(a)
    else:
        rectangle = Rectangle(a, b)
    shapes.add_shape(rectangle)


def new_regular(shapes, shape_name):
    '''Function that instantiates a regular pentagon object.'''
    a = int(input("Enter side's length >"))
    if shape_name.lower() == "square":
        square = Square(a)
        shapes.add_shape(square)
    elif shape_name.lower() == "regular pentagon":
        regular_pentagon = RegularPentagon(a)
        shapes.add_shape(regular_pentagon)
    else:
        raise ValueError


def new_shape(shapes):
    '''Function asks for input and then creates objects accordingly to users choice'''
    while True:
        shape_name = input("""
    What kind of shape do you want to add? (Enter q for Main Menu)
    [Circle, Triangle, Rectangle, Square, Regular pentagon]
        >""")
        if shape_name.lower() == "q":
            break
        try:
            if shape_name.lower() == "circle":
                new_circle(shapes)
            elif shape_name.lower() == "triangle":
                new_triangle(shapes)
            elif shape_name.lower() == "rectangle":
                new_rectangle(shapes)
            elif shape_name.lower() == "square":
                new_regular(shapes, shape_name)
            elif shape_name.lower() == "regular pentagon":
                new_regular(shapes, shape_name)
            else:
                print ("Shape not recognised. Try again")
        except ValueError:
            print("Not a valid number. Try again")


def show_formulas():
    '''Function asks for user's input and then show formula for needed shape'''
    while True:
        formula = input (show_formula)
        if formula.lower() == "0":
            break
        try:
            if formula == "1":
                print("Circle formulas: {}  & {}".format(Circle.get_area_formula(), Circle.get_perimeter_formula()))
            elif formula == "2":
                print("Triangle formulas: {}  & {}".format(Triangle.get_area_formula(), Triangle.get_perimeter_formula()))
            elif formula == "3":
                print("Rectangle formulas: {}  & {}".format(Rectangle.get_area_formula(), Rectangle.get_perimeter_formula()))
            elif formula == "4":
                print("Square formulas: {}  & {}".format(Square.get_area_formula(), Square.get_perimeter_formula()))
            elif formula == "5":
                print("Regular Pentagon formulas: {}  & {}".format(RegularPentagon.get_area_formula(), RegularPentagon.get_perimeter_formula()))
            else:
                print("Shape not recognised. Try again")
        except ValueError:
            print("Not a valid number. Try again")


def main():
    '''Main body of the program. It shows menu and lets you navigate through user options'''

    shapes = ShapeList()  # object containing all shapes added by the user

    while True:
        print (menu_options)
        # TODO: implement user interaction here. You can change the code below
        option = input("Select an option: ")
        if option == "1":
            # Add new shape
            new_shape(shapes)
        elif option == "2":
            # Show all shapes
            print (shapes.get_shapes_table())
        elif option == "3":
            # Show shape with the largest perimeter
            print(shapes.get_largest_shape_by_perimeter())
        elif option == "4":
            # Show shape with the largest area
            print(shapes.get_largest_shape_by_area())
        elif option == "5":
            # Show formulas
            show_formulas()
            pass
        elif option == "0":
            sys.exit()

if __name__ == "__main__":
    main()
