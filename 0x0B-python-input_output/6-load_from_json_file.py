#!/usr/bin/python3
"""Defines load_from_json_file. """
import json


def load_from_json_file(filename):
    """prints an object."""
    with open(filename) as f:
        return json.load(f)
