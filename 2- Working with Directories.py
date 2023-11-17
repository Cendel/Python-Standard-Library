from pathlib import Path

# we have a path object that represents a directory:
path = Path(r"test_folder")
# A few useful methods:
print(path.exists())
# path.mkdir()  # => creates a directory
# path.rmdir()  # => removes a directory
# path.rename(r"C:\Users\cende\Desktop\")  # => renames

# with the following iterdir() method, we can get the list of files and directories in the path
for p in path.iterdir():
    print(p)

# if we use list comprehension:
paths = [p for p in path.iterdir()]
print(paths)

# now, let take only the directories:
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# iterdir() method is pretty useful but it has two limitations:
# 1- it cannot search by pattern, and 2- it cannot search recursively
# we can use glob method for these functionalities:

paths = [p for p in path.glob("*.py")]
print(paths)

paths = [p for p in path.rglob("*.py")]  # rglob is short for recursive glob
print(paths)
