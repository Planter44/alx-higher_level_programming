#!/usr/bin/python3
"""Script that takes in a URL and Sends a request to the URL to display the value of X"""

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
