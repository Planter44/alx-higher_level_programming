#!/usr/bin/python3
""" Defines append_after. """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line. if string encountered """

    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_line))
