# Program Name: datetime.py
# Programmer: Denis Carr
# Date: March 2019

# import datetime package
from datetime import datetime

# get current date and time
now = datetime.now()

#get day part of time and convert to int
day = int(now.strftime("%d"))

# get am/pm in lower case
ampm=now.strftime("%p").lower()

# get the extension: st, nd, rd or th for the day, depending on what day of the month it is
ext=""
if day == 1:
    ext="st"
elif day == 2:
    ext="nd"
elif day == 3:
    ext="rd"
else:
    ext="th"

# print the date and time in required format
print(now.strftime("%A, %B %d"+ext+" %Y at %-I:%M"+ampm))