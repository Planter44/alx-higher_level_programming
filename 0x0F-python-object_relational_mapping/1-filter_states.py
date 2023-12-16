#!/usr/bin/python3
"""
The script lists all the states
"""

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
