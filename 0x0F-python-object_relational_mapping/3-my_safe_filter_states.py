#!/usr/bin/python3
"""Script that lists all values in states where name matches the argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Make connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    """Cursor object lets us execute sql queries"""
    cur = db.cursor()

    """Execute the MySQL query"""
    cur.execute("SELECT * FROM states \
                 WHERE name = %(name)s \
                 ORDER BY id ASC \
                 ", { "name": argv[4] })

    """Used after SELECT statement to obtain results"""
    rows = cur.fetchall()

    """If statement checks that name exists"""
    if rows is not None:
        """For loop to display results"""
        for row in rows:
            print(row)

    """Clean up process"""
    cur.close()
    db.close()
