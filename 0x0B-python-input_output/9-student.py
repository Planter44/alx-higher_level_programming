#!/usr/bin/python3
""" Defines class sudent.
"""


class Student:
    """ Class student """

    def __init__(self, first_name, last_name, age):
          """ Initializing """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns description """
        return self.__dict__.copy()