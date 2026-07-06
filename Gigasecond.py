# This code takes a date and returns the date after one gigasecond.
# This can easily be generalized for any length of time.
import datetime as dt
def add(moment):
    return moment + dt.timedelta(seconds = 1e9)
