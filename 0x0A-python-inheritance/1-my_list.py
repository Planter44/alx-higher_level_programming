#!/usr/bin/python3
"""
The myList class
"""


class MyList(list):
    def __init__(self):
        """super init"""
        super().__init__()

    def print_sorted(self):
        """sorted list"""
        print(sorted(self))
