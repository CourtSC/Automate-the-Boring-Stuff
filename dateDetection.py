'''
Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
'''

import re

# Detect dates in DD/MM/YYY format.
# Store these strings into variables named month, day, and year.
# Write additional code that can detect if it is a valid date.

dateRegex = re.compile(r'''(
    ([0-3][0-9])      # Day
    /
    ([0-1][0-9])      # Month
    /
    ([1-2][0-9]{3})   # Year
)''', re.VERBOSE)

while True:
    mo = dateRegex.search('Enter a date in DD/MM/YYYY format: ') # Matches date.
    try:
        date, day, month, year = mo.groups() # Assigns date to variables.
        exit
    except:
        print('Not a valid date.')

if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    leapYear = True
else:
    leapYear = False

if int(year) in range(1000,3000): # Check for valid year.
    if (int(month) in [4, 6, 9, 11]) and (int(day) in range(1, 31)): # Check for 30 day month.
        print(date)
    elif (int(month) == 2): # Check for February.
        if leapYear and (int(day) in range(1,30)): # Check for 29 day Leap Year.
            print(date)
        elif not leapYear and (int(day) in range(1,29)): # Check for 28 day not Leap Year.
            print(date)
    elif (int(month) in range(1,13)) and (int(day) in range(1,32)): # Check for 31 day month.
        print(date)
    else:
        print('Not a valid date')