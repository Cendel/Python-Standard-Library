# in datetime module we also have a class timedelta, which represents a duration.

from datetime import datetime, timedelta

# when we subtract the following dates, we get a timedelta object:
dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
duration = dt2 - dt1
print(duration)

# the timedelta object has a few interesting attributes:
print(duration.days)
print(duration.seconds) # seconds, the seconds of the years not included
print(duration.total_seconds())  # seconds + seconds of the days

# we can also add a timedelta object to a datetime object:
dt3 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt3)