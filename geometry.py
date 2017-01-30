import math

'''
There are some @classmethods like get_area or get_perimeter below.
They have to be available to whole class instead of just an instance because
you run them on classes not particular objects.
'''


class Shape:
    """
    This is an abstract class representing geometrical shape.
    """

    def __init__(self, name):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """

    @classmethod
    def get_area(cls):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        pass

    @classmethod
    def get_perimeter(cls):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        pass

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information bout shape
        """
        return "Shape name: {}".format(self.name)

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the shape as a string.

        Returns:
            str: area formula
        """
        pass

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the shape as a string.

        Returns:
            str: perimeter formula
        """
        pass


class Circle(Shape):
    '''This class inherits from Shape and creates a circle object'''
    def __init__(self, r):
        if r <= 0:
            raise ValueError
        self.name = "Circle"
        self.r = r
        self.area = (math.pi * (r**2))
        self.perimeter = (2 * math.pi * r)

    def __str__(self):
        return ("Circle, r = {}.".format(self.r))

    def get_perimeter(self):
        return self.perimeter

    def get_area(self):
        return self.area

    @classmethod
    def get_area_formula(self):
        return "Area = π × r**2"

    @classmethod
    def get_perimeter_formula(self):
        return "Perimeter = 2 × π × r"

class Triangle(Shape):
    '''This class inherits from Shape and creates a triangle object'''
    def __init__(self, a, b, c):
        if a <=0 or b <= 0 or c <=0:
            raise ValueError
        self.name = "Triangle"
        self.a = a
        self.b = b
        self.c = c
        s = ((a + b + c) / 2)
        self.area = (math.sqrt(s * ((s-a) * (s-b) * (s-c))))
        self.perimeter = a + b + c

    def __str__(self):
        return ("Triangle, a = {}, b = {}, c = {}.".format(self.a, self.b, self.c))

    def get_perimeter(self):
        return self.perimeter

    def get_area(self):
        return self.area

    @classmethod
    def get_area_formula(self):
        return "Area = sqrt(s(s-a)(s-b)(s-c))"

    @classmethod
    def get_perimeter_formula(self):
        return "Perimeter = a + b + c"


class EquilateralTriangle(Triangle):
    '''This class inherits from Triangle and creates a equilateral triangle object'''
    def __init__(self, a):
        if a <= 0:
            raise ValueError
        self.name = "Equilateral Triangle"
        self.a = a
        self.b = self.a
        self.c = self.a
        self.s = (3*a) / 2
        self.area = math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
        self.perimeter = 3*a

    def __str__(self):
        return ("Equilateral Triangle, a = {}.".format(self.a))

    def get_perimeter(self):
        return self.perimeter

    def get_area(self):
        return self.area

    @classmethod
    def get_area_formula(self):
        return "Area = sqrt(s(s-a)(s-b)(s-c))"

    @classmethod
    def get_perimeter_formula(self):
        return "Perimeter =  a + b + c"


class Rectangle(Shape):
    '''This class inherits from Shape and creates a rectangle object'''
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError
        self.name = "Rectangle"
        self.a = a
        self.b = b
        self.area = a*b
        self.perimeter = 2*a + 2*b

    def __str__(self):
        return ("Rectangle, a = {}, b = {}.".format(self.a, self.b))

    def get_perimeter(self):
        return self.perimeter

    def get_area(self):
        return self.area

    @classmethod
    def get_area_formula(self):
        return "Area = a * b"

    @classmethod
    def get_perimeter_formula(self):
        return "Perimeter = 2a + 2b"


class Square(Rectangle):
    '''This class inherits from Rectangle and creates a square object'''
    def __init__(self, a):
        if a <= 0:
            raise ValueError
        self.name = "Square"
        self.a = a
        self.b = self.a
        self.area = a*a
        self.perimeter = 4*a

    def __str__(self):
        return ("Square, a = {}".format(self.a))

    def get_perimeter(self):
        return self.perimeter

    def get_area(self):
        return self.area

    @classmethod
    def get_area_formula(self):
        return "Area = a * a"

    @classmethod
    def get_perimeter_formula(self):
        return "Perimeter = 4a"


class RegularPentagon(Shape):
    '''This class inherits from Shape and creates a regular pentagon object'''
    def __init__(self, a):
        if a <= 0:
            raise ValueError
        self.name = "Regular Pentagon"
        self.a = a
        self.area = (a**2 * math.sqrt(5*(5+2 * math.sqrt(5))))/4
        self.perimeter = round(5*a, 2)

    def __str__(self):
        return ("Regular Pentagon, a = {}.".format(self.a))

    def get_perimeter(self):
        return self.perimeter

    def get_area(self):
        return self.area

    @classmethod
    def get_area_formula(self):
        return "Area =  (a2 sqrt(5(5+2sqrt(5))))/4"

    @classmethod
    def get_perimeter_formula(self):
        return "Perimeter = 5a"


class ShapeList:
    '''This class contains all shapes added by the user'''
    def __init__(self):
        self.shapes = []

    def get_largest_shape_by_perimeter(self):
        '''Function returns shape with a highest perimeter'''
        max_perimeter = 0
        for i in range(len(self.shapes)):
            for shape in self.shapes:
                if shape.get_perimeter() > max_perimeter:
                    max_perimeter = shape.get_area()
                    max_shape = shape
                else:
                    continue
        return (max_shape)

    def get_largest_shape_by_area(self):
        '''Function returns shape with a highest area'''
        max_area = 0
        for i in range(len(self.shapes)):
            for shape in self.shapes:
                if shape.get_area() > max_area:
                    max_area = shape.get_area()
                    max_shape = shape
                else:
                    continue
        return (max_shape)

    def add_shape(self, shape):
        '''Function adds a new shape. It is used when creating new shapes.'''
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            raise TypeError("Shape not recognised.")

    def get_shapes_table(self):
        '''This function returns a string formatted table with the most important attributes'''
        area_list = []
        perimeter_list = []
        classname_list = []
        perim_formula_list = []
        area_formula_list = []
        str_list = []
        index_list = []
        index = 0

        for shape in self.shapes:
            area_list.append(str(shape.get_area()))
            perimeter_list.append(str(shape.get_perimeter()))
            classname_list.append(shape.name)
            perim_formula_list.append(shape.get_perimeter_formula())
            area_formula_list.append(shape.get_area_formula())
            str_list.append(str(shape))
            index_list.append(str(index))
            index += 1

        class Table:
            '''Creates an instance of a Table class columns with a cleaver output. Warning: Dragons and magic lives here.
            Source: http://code.activestate.com/recipes/577202-render-tables-for-text-interface/'''
            def __init__(self, *columns):
                self.columns = columns
                self.length = max(len(col.data) for col in columns)

            def get_row(self, rownum=None):
                for col in self.columns:
                    if rownum is None:
                        yield col.format % col.name
                    else:
                        yield col.format % col.data[rownum]

            def get_line(self):
                for col in self.columns:
                    yield '-' * (col.width + 2)

            def join_n_wrap(self, char, elements):
                return ' ' + char + char.join(elements) + char

            def get_rows(self):
                yield self.join_n_wrap('+', self.get_line())
                yield self.join_n_wrap('|', self.get_row(None))
                yield self.join_n_wrap('+', self.get_line())
                for rownum in range(0, self.length):
                    yield self.join_n_wrap('|', self.get_row(rownum))
                yield self.join_n_wrap('+', self.get_line())

            def __str__(self):
                return '\n'.join(self.get_rows())

            class Column():
                LEFT, RIGHT = '-', ''

                def __init__(self, name, data, align=RIGHT):
                    self.data = data
                    self.name = name
                    self.width = max(len(x) for x in data + [name])
                    self.format = ' %%%s%ds ' % (align, self.width)

        Column = Table.Column
        return str(Table(
            Column('idx', index_list),
            Column('Class', classname_list),
            Column('__str__', str_list, align=Column.LEFT),
            Column("Perimeter", perimeter_list),
            Column("Formula", perim_formula_list, align=Column.LEFT),
            Column("Area", area_list),
            Column("Formula", area_formula_list, align=Column.LEFT)))

