from pathlib import Path
from time import ctime
import shutil

path = Path(r"test_folder\pytho_test_file.py")
print(path.exists())
# path.rename(r"C:\Users\cende\Desktop\test_folder\test_python_file.py")
# path.unlink() # => deletes the file
print(path.stat())  # returns information about the file (size, last access/modification/creation time,etc.)
# to turn the time values into human-readable format, we can => from time import ctime   and:
print(ctime(path.stat().st_ctime))
# in the above code, we printed the creation time of the file in human-readable format

# We also have a couple methods for reading data from a file:
# print(path.read_bytes())   # return the content of the file as bytes object when representing binary data
# print(path.read_text()) # returns the content of the file as a string
# path.write_text("....")   # used to write textual data to a file
# path.write_bytes()
# with the above read/write methods, files are automatically opened and closed, so we don't have
# to worry about opening and closing files, which makes these methods pretty useful.

# However, when it comes to copying a file, this path object is not the ideal way to copy a file:
target = Path(r"test_folder\test_file.txt")
#target.write_text(path.read_text())  # we copied the content of the file into another file

# the following way is easier and cleaner when copying a file:
# import shutil # this module supplies a number of high level operations for copying and moving files

shutil.copy(path, target)




# NOTE:
# the above way of reading a file (path.read_text()) is easier than using open method, in which case, we also have to specify
# the mode and then have to use the close method:
"""
file = open(file_path, 'r')  # 'r' denotes read mode
content = file.read()
print(content)  # Display file content
file.close()    # Close the file after reading
"""

"""
NOTE: Using with open() is generally considered a better practice for handling files in Python because it takes care 
of closing the file automatically, reducing the chance of leaving files open unnecessarily and 
ensuring proper resource management. So best practice:

with open(file_path, 'r') as file:  # 'r' denotes read mode
    content = file.read()
    print(content)  # Display file content
"""