#!/usr/bin/python3
"""Contains subclass named Rectangle"""


from models.base import Base


class Rectangle(Base):
    """subclass Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width

    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.__height

    @property
    def x(self):
        """getter for private instance attribute x"""
        return self.__x

    @property
    def y(self):
        """getter for private instance attribute y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter for private instance attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter for private instance attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area value of Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints Rectangle instance with the # char"""
        string = ""
        print(self.y * "\n", end="")
        for i in range(self.height):
            string += str(self.x * " ")
            for j in range(self.width):
                string += "#"
            if i != self.height - 1:
                string += "\n"
        print(string)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and args is not None:
            for i, a in enumerate(args):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dict representation of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
