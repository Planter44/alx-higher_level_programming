#!/usr/bin/python3
"""Module containing write_file function"""


def write_file(filename="", text=""):
    """Puts a string to UTF8 text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
