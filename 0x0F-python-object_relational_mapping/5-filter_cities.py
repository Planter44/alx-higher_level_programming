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
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name)
    cur = db.cursor()

        cur.execute("""
            SELECT
                c.id, c.name
            FROM
                c cities
            JOIN
                states
            ON
                c.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                c.id ASC
        """, (state_name, ))
    rows = cur.fetchall()

    for i in range(len(rows)):
        print(rows[i][0], end=", " if i + 1 < len(rows) else "")
    print("")
