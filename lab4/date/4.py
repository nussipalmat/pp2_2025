#Write a Python program to calculate two date difference in seconds.

import datetime as dt

date1 = dt.datetime(2018,3,24,0,0,0)
date2 = dt.datetime(2024,2,6,0,0,0)

date_diff = date2 - date1

print(date_diff.total_seconds())
