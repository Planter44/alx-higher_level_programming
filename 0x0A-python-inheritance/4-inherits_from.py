#!/usr/bin/python3
"""The
inherits_from function.
"""


def inherits_from(obj, a_class):
    """Returns to issubclass"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
