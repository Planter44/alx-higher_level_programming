#!/usr/bin/python3
"""" Script that takes in a URL and Sends a request to the URL to display X"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as page:
        print(page.getheader("X-Request-Id"))
