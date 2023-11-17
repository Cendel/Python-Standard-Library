# basically, we have two modules for working with date and time. "time" module which gives
# us a time stamp, and "datetime" which gives us date time objects with attributes like year,
# month, and so on. Here, we are going to look at "time" module:

import time

print(time.time())  # returns the current date time as a time stamp, a floating point number


# that represents the number of seconds from the beginning of a point in time that is set by
# operating system. This is not human-readable. We use it to perform calculations. For example:

# imagine we send an email to 2000 recipients:
def send_emails():
    for i in range(100000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)  # amount of time to execute the function
