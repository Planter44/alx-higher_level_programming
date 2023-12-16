#!/usr/bin/python3
"""
The script lists all the cities
"""

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
    cur.execute("SELECT c.id, c.name, s.name \
                 FROM cities c INNER JOIN states s \
                 ON c.state_id = s.id \
                 ORDER BY c.id")
        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
