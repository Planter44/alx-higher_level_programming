#!/usr/bin/python3
"""
MyInt function.
"""


class MyInt(int):
    """Defines MyInt class"""

    def __init__(self, value):
        """MyInt class"""
        self.value = value

    def __eq__(self, other):
        """__eq__ operator"""
        return self.value != other

    def __ne__(self, other):
        """__ne__ operator"""
        return self.value == other
