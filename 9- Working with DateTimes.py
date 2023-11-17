from datetime import datetime
import time

dt = datetime(2018, 1, 1)  # returns a specified datetime
print(dt)

dt = datetime.now()  # returns the current datetime
print(dt)

datetime.strptime("2018/01/01", "%Y/%m/%d")  # parses a date time string.
# This is particularly useful when we get input from the user or read it from the file. In bot
# these scenarios we are dealing with strings. For more: https://docs.python.org/3/library/datetime.html

# we can also convert a time stamp into a date time object:
# first => import time
dt = datetime.fromtimestamp(time.time())
print(dt)

# datetime object has different attributes:
print(f"{dt.year}/{dt.month}")

# we also have a method for formatting date times:
print(dt.strftime("%Y/%m"))  # converts a datetime object into a string. So this method is the
# opposite of strptime() method

# we can also compare datetime objects:
dt = datetime(2018, 1, 1)
dt1 = datetime(2022, 1, 1)
print(dt > dt1)