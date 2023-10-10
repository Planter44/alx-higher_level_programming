#!/usr/bin/python3
"""adds all arguments to a Python list"""


import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(filename):
    lock = load_from_json_file(filename)
else:
    lock = []
obj.extend(sys.argv[1:])
save_to_json_file(lock, filename)
