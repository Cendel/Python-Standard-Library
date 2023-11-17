# SQLite is a lightweight database. It is often the preferred technology for small applications
# like the mobile apps.

import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
print(movies)  # we have a list of dictionaries

# now we are going to store this list in the database:
# we create a database, create a connection to this database, and give a name to this connection
# (conn). We use "with" syntax because this connection should be closed after we are done with it.
# (at this step, we created a table in SQLite using the interface of SQLite database)
"""
with sqlite3.connect("my_db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"  # "?" are placeholders for the values
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()
"""

# in order to read data from the database:
with sqlite3.connect("my_db.sqlite3") as conn:
    command = "SELECT * FROM Movies"  # "?" are placeholders for the values
    mycursor = conn.execute(command)   # when we read data from database, we get cursor. A cursor is
    # an iterable object.
    for row in mycursor:
        print(row)  # we get a tuple of values
    # the following method returns all the values in the table in one go
    # print(mycursor.fetchall())
