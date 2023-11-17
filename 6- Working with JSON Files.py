# JSON = JavaScript Object Notation (a popular way to represent data in human-readable form

import json
from pathlib import Path

# let's create an array of movie objects:
movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990},
]

data = json.dumps(movies)  # converts the Python object "movies" into a JSON formatted string
print(data)
# NOTE: in this case, the output happens to be identical to the syntax that we use to define an array of
# dictionaries in Python. But this is not the case when working with other languages.

# we can write it to a file. First, we import => from pathlib import Path
Path("movies.json").write_text(data)

# Let's imagine we get this json file from somewhere else:
data = Path("movies.json").read_text()  # we read all the text in json file and store it in data variable
print(type(data))  # remember that data is a string that includes data which is  formatted as json.

# we parse this string into an array of objects:
movies = json.loads(data)  # this will return an array of dictionaries
print(movies)
print(movies[0])
print(movies[0]["title"])
