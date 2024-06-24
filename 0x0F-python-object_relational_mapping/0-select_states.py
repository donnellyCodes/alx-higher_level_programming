#!/usr/bin/python3

"""
A script that lists all states from te database hbtn_0e_0_user
It takes three arguments username, password and database name
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="Localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    data = cur.fetchall()
    for row in data:
        print(row)

    cur.close()
    db.close()
