#!/usr/bin/python3
"""
add_attribute function
"""


def add_attribute(object, fun, val):
    """ The add_attribute function """
    if not hasattr(object, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(object, fun, val)
