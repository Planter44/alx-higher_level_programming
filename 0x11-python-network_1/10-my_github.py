#!/usr/bin/python3
"""Script that takes your github details and uses the git API to dispaly your ID."""

import requests
from sys import argv

if __name__ == "__main__":
    auth = (argv[1], argv[2])
    request = requests.get("https://api.github.com/user", auth=auth)
    print(request.json().get("id"))
