#!/usr/bin/python3
"""" Script that takes the URL and email, sending a POST resquest to the URL"""
if __name__ == '__main__':
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
