#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Make connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    """Cursor object lets us execute sql queries"""
    cur = db.cursor()

    """Execute the MySQL querie"""
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """Used after SELECT statement to obtain results"""
    rows = cur.fetchall()

    """For loop to display results"""
    for row in rows:
        print(row)

    """Clean up process"""
    cur.close()
    db.close()
