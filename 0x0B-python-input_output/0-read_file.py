#!/usr/bin/python3
"""Contains function that read_file"""


def read_file(filename=""):
    """Prints content of the UTF8 text file."""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
