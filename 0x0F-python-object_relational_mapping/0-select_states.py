#!/usr/bin/env python3

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command-line argument
    mysql_username = sys.argv[1]
    mysql_pswd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the mysql database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_pswd, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to select all states order by ID
    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    # Fetch all rows from the executed query
    states = cursor.fetchall()

    # print each state
    for state in states:
        print(state)

    # close the cursor and database connection
    cursor.close()
    # disconnect database
    db.close()
