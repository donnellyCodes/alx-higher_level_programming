#!/usr/bin/python3
"""
 script that lists all states with a name starting with N from the database hbtn_0e_0_usa
 It takes three arguments username, password and database name
 """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
