#!/usr/bin/python3
"""
Subclass Rectangle and class BaseGeometry.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the Square class."""
    def __init__(self, size):
        """Checks and sets the default attributes of Square class."""
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """Setting str behaviour"""
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size
