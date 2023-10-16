#!/usr/bin/python3
"""Contains the Rectangle module."""
from models.base import Base


class Rectangle(Base):
    """class Rectangle from Base and defines a Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing default attributes of Base object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Overridding default behaviour of the __str__ """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    # width attribute getter and setter.
    @property
    def width(self):
        """Get and set the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width attribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height attribute getter and setter.
    @property
    def height(self):
        """Get and set the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x attribute getter and setter.
    @property
    def x(self):
        """Get and set x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """set x attribute."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y attribute getter and setter.
    @property
    def y(self):
        """Get the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y attribute."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Methods
    def area(self):
        """Returning area value."""
        return self.width * self.height

    def display(self):
        """Prints in stdout Rectangle instance with the character #"""
        for new_line in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    def update(self, *args, **kwargs):
        """Updates these attributes
        """
        dct = {}
        if args is not None and len(args) > 0:
            keys = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args) if len(args) <= 5 else 5):
                dct[keys[i]] = args[i]
        else:
            dct = kwargs

        if len(dct) > 0:
            for key, value in dct.items():
                if key == 'id' and value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returnning the dictionary."""
        return {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y
        }
