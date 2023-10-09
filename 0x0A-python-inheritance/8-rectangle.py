#!/usr/bin/python3
"""
The BaseGeometry Function.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines class rectangle"""
    def __init__(self, width, height):
        """The rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
