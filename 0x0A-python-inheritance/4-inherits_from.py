#!/usr/bin/python3
"""
The inherits_from function
"""


def inherits_from(obj, a_class):
    """True if obj is subclass of a_class"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
