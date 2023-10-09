#!/usr/bin/python3
""" Module containing a append_write function
"""


def append_write(filename="", text=""):
    """String appened at the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
