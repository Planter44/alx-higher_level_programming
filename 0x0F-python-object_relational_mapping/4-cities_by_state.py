#!/usr/bin/python3
"""
The script lists all the cities
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                 FROM cities c INNER JOIN states s \
                 ON c.state_id = s.id \
                 ORDER BY c.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
