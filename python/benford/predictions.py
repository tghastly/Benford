"""

Benford's predictions for the relative frequencies of numbers.

Successive digit positions are considered individually,
starting with the significand and proceeding from left to right
towards the least significant digit position.

"""


# The significand ranges from 1 thru 9 inclusive (0 is excluded)

FIRST_DIGIT_PERCENTAGES = [
    30.1,    # '1'
    17.6,
    12.5,
    9.7,
    7.9,
    6.7,
    5.8,
    5.1,
    4.5]   # '9'

# 2nd and subsequent digits range from 0 thru 9 inclusive
# (0 is included)

SECOND_DIGIT_PERCENTAGES = [
    12.0,  # '0'
    11.4,
    10.9,
    10.4,
    10.0,
    9.7,
    9.3,
    9.0,
    8.8,
    8.5]    # '9'