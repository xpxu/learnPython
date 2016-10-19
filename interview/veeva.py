
def isLeapYear(y):
    if y % 100 and not y % 4:
        return True
    elif y % 400:
        return True
    else:
        return False

def dayOfYear(year, month, day):
    '''
    Given a specific date, return the day of the year for that date.
    '''
    days_leap_year = \
        [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_nonleap_year = days_leap_year[:]
    days_nonleap_year[2] = 28
    num = lambda x: sum(x[:month]) + day
    if isLeapYear(year):
        return num(days_leap_year)
    else:
        return num(days_nonleap_year)


print dayOfYear(2016, 1, 3)
print dayOfYear(2016, 2, 1)
print dayOfYear(2016, 12, 3)
print dayOfYear(2016, 12, 31)
