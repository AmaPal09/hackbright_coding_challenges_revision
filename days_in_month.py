# Given a string with a month and a year (separated by a space), return the 
# number of days in that month.

# Leap years are a bit tricky. A year is a leap year if and only if:
# it is evenly divisible by 4
# except if it is divisible by 100, in which case it isn’t
# except if it is divisible by 400, in which case it is
# So, for example, 1904 was a leap year. 1900 is divisible by 100, so it wasn’t. 
# 2000 is divisible by 400, so it was.

MONTH_DAYS_DICT = {
                    "01": 31, "02": 28, "03": 31, "04": 30,
                    "05": 31, "06": 30, "07": 31, "08": 31,
                    "09": 30, "10": 31, "11": 30, "12": 31
                    }

def is_leap_year(year): 
    """ Is this a leap year? 
        
        I/P: Year as Int 
        O/P: Binary(T/F)

        Every 4 years is a leap year 
        Except every hundred years 
        Except-except every 400::
        >>> is_leap_year(1904)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2000)
        True
 
    """

    if year % 400 == 0: 
        return True
    if year % 100 == 0: 
        return False 
    if year % 4 == 0: 
        return True 
    return False 

def days_in_month(date): 
    """How many days are there in a month?
    
        I/P: String (With month and date as "01 2016" format for January 2016)
        O/P: Int 
    
        >>> days_in_month("02 2015")
        28
        >>> days_in_month("02 2016")
        29
        >>> days_in_month("01 2013")
        31
        >>> days_in_month("08 2017")
        31
        >>> days_in_month("02 1908")
        29
        >>> days_in_month("02 1700")
        28
        >>> days_in_month("02 2000")
        29
    
    """

    month, year = date.strip().split(" ")
    if is_leap_year(int(year)) and month == "02": 
        return 29 
    else: 
        return MONTH_DAYS_DICT[month]

# Runtime O(n)


def days_in_month_hb(date):
    """How many days are there in a month?
        >>> days_in_month_hb("02 2015")
        28
        >>> days_in_month_hb("02 2016")
        29
        >>> days_in_month_hb("01 2013")
        31
        >>> days_in_month_hb("08 2017")
        31
        >>> days_in_month_hb("02 1908")
        29
        >>> days_in_month_hb("02 1700")
        28
        >>> days_in_month_hb("02 2000")
        29
    """

    # START SOLUTION

    month, year = date.split()
    month = int(month)
    year = int(year)

    # Account for February

    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31

    if month in {4, 6, 9, 11}:
        return 30


if __name__ == '__main__': 
    import doctest 

    result = doctest.testmod()

    if result.failed == 0: 
        print("ALL TEST PASSED")

