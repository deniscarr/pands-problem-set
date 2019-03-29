# Program Name: begins-with-t.py
# Programmer: Denis Carr
# Date: March 2019

#import required libraries
from datetime import datetime

# get the current time
now = datetime.now()

# get the day part
day = now.strftime("%A")

# day starts with T i.e. if index 0 is T
if day[0]=='T':
    print("Yes - today begins with a T.")
else:
    print("No - today does not begin with a T.")