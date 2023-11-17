from pathlib import Path
from zipfile import ZipFile

# we create a zip file (named files.zip) in the current folder and assign a reference (myzip) to it:
myzip = ZipFile("files.zip", "w")

# we get all the files in test_folder and write them into the zip file:
for path in Path("test_folder").rglob("*.*"):
    myzip.write(path)
myzip.close()

# the following is a better practice than the above:
with ZipFile("files.zip", "w") as myzip:
    for path in Path("test_folder").rglob("*.*"):
        myzip.write(path)

# in order to read its content:
with ZipFile("files.zip") as myzip:
    print(myzip.namelist())  # returns the list of all the files in myzip
    info = myzip.getinfo("test_folder/pytho_test_file.py")  # get the info of a specific file
    print(info.file_size)
    print(info.compress_size)
    # myzip.extractall("some_directory_name")   # extracts all the files from the myzip file to
    # the given directory ("some_directory_name")
    
