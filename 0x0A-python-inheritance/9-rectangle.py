#!/usr/bin/python3
"""
Subclass Rectangle and class BaseGeometry.
"""


class BaseGeometry:
    """Defines the BaseGeometry Class"""
    def area(self):
        """raising an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is an integer or greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines Rectangle class"""
    def __init__(self, width, height):
        """The rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returning the area"""
        return self.__width * self.__height

    def __str__(self):
        """informal srting to the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
