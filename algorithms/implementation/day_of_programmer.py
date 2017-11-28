"""
https://www.hackerrank.com/challenges/day-of-the-programmer/problem

1700 - 1918: Julian calendar
1918 - 2700: Gregorian calendar

TODO: Refactor this.
"""

from datetime import datetime, timedelta


def is_leap_year(year, calendar_type):
    if calendar_type == JULIAN_CALENDAR:
        if year % 4 == 0:
            return True
        else:
            return False
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

NON_LEAP_YEAR_256DAY_MONTH = 9  # September
NON_LEAP_YEAR_256DAY_DAY = 13

JULIAN_CALENDAR = 1
GREGORIAN_CALENDAR = 2
TRANSITION = 3

year = int(input().strip())

if year < 1918:
    calendar_type = JULIAN_CALENDAR
elif year > 1918:
    calendar_type = GREGORIAN_CALENDAR
else:
    calendar_type = TRANSITION

non_leap_year_date = datetime(
    year,
    NON_LEAP_YEAR_256DAY_MONTH,
    NON_LEAP_YEAR_256DAY_DAY,
)

if calendar_type == TRANSITION:
    # 1918 had less 13 days (it went from Jan 31 directly to 14 Feb)
    day256 = non_leap_year_date + timedelta(13)
elif is_leap_year(year, calendar_type):
    day256 = non_leap_year_date - timedelta(1)
else:
    day256 = non_leap_year_date

print(day256.strftime('%d.%m.%Y'))
