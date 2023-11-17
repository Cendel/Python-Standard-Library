from pathlib import Path  # we imported Path class from pathlib

# for documentation => https://docs.python.org/3/library/pathlib.html

print(Path.home())

a = Path(r"C:\Users\cende\Desktop\test_folder")
# SIDE NOTE: In Python, a raw string is a special type of string that allows you to include
# backslashes (\\) without interpreting them as escape sequences1. This means that you don’t need to
# escape characters in a raw string, as it will treat backslashes as literal characters1.

print(a)

path = Path(r"C:\Users\cende\Desktop\Beginning Programming For Dummies.pdf")
print(path.exists())  # checks if path exists or not
print(path.is_file())  # checks if path is a file or not
print(path.is_dir())  # checks if path is a directory or not
print(path.name)  # returns the name of file/folder
print(path.stem)  # returns the name of file/folder without extension
print(path.suffix)  # returns the extension of file
print(path.parent)  # returns the parent of file/folder

# we can use "with_name" method to create a new path based on this existing path but only
# change the name and the extension of the file:
path = path.with_name("file.txt")  # returns the extension of file
print(path)
# we can also get the absolute value of this path:
print(path.absolute())
# Note: The file (file.txt) doesn't exist yet, this only represents its path.

# Similar to this with_name, we have another method with_suffix used to change the extension of a file.
path = path.with_suffix(".pdf")
print(path)
# Note again that we didn't rename the file, we are only representing a path object.
