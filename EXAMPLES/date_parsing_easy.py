#!/usr/bin/env python
from dateutil import parser
from dateutil.tz import gettz

ist = gettz('Asia/Kolkata')
ny = gettz('America/New_York')
tzinfo = {'IST': ist, 'EDT': ny}

date_strings = [  # <1>
    'April 1, 2015',
    '4/1/2015',
    'Apr 1, 2015',
    'Apr 1 2015',
    '04/01/2015',
#    '04/05/2021 EDT',
    "Apr 5 '21",
    '1 Apr 2015',
    'April 1st, 2015',
    'April 1, 2015 8:09',
    '4/1/2015 8:09 PM',
    'Apr 1, 2015 5 AM',
    'Apricot 4, 2021',
    'Feb 29, 2021',
    'March 32, 1897',
   'Apr 5, 2021 7:30PM IST'
]

for date_string in date_strings:
    print(f"{date_string:25}", end=' ')
    try:
        dt = parser.parse(date_string, tzinfos=tzinfo)  # <2>
        print(dt)
    except ValueError as err:
        print("Can't parse")
