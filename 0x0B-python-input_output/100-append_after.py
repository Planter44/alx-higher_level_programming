#!/usr/bin/python3
""" Defines append_after. """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line. if string encountered """

    res_line = []
    with open(filename, 'a', encoding="utf-8") as b:
        for line in b:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'c', encoding="utf-8") as b:
        b.write("".join(res_line))
