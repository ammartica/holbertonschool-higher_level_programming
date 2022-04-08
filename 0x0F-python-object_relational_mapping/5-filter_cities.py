#!/usr/bin/python3
"""Script that lists cities of a state that it takes as an argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Make connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    """Cursor object lets us execute sql queries"""
    cur = db.cursor()

    """Execute the MySQL querie"""
    cur.execute("SELECT cities.name FROM cities \
                 INNER JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s", (argv[4], ))

    """Used after SELECT statement to obtain results"""
    rows = cur.fetchall()

    """For loop joins cities, after prints them"""
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    """Clean up process"""
    cur.close()
    db.close()
