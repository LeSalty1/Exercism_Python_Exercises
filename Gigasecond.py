# This code takes a date and returns the date after one gigasecond.
import datetime as dt
def add(moment):
    return moment + dt.timedelta(seconds = 1e9)
