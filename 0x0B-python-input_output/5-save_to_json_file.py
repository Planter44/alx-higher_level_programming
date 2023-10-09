#!/usr/bin/python3
"""
Defines save_to_json_file function.
"""
import json


def save_to_json_file(my_obj, filename):
    """prints an object."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
