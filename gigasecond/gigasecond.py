# GIGASECOND ANNIVERSARY
# LANGUAGE: PYTHON

# Write a function that will calculate
# the date that someone will celebrate their 1 gigasecond anniversary.

# Note: A gigasecond is one billion (10**9) seconds.

# The input is three parameters representing someone's birthday.

# As a convenience for celebration planning,
# the function should also calculate the day of
# the week and the number of days from today.

# The output should be an array formatted as such:
# ["YYYY-MM-DD", 'day_of_the_week', days_until]

# You can google datetime in python to familiarize yourself with it


# Examples:

# gigasecond(1988, 5, 15) # ["2020-01-22", "Wednesday", "1764 days left"]
# gigasecond(2015, 2, 17) # ["2046-10-26", "Friday", "11538 days left"]


from datetime import date, timedelta


WEEKDAYS = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday")


def get_user_b_date(year, month, day):

    # getting to be lived before giga_second
    giga_birthsecond = date(year, month, day) + timedelta(seconds=10 ** 9)

    # calling on import datetime using WEEKDAYS list
    anniversary = WEEKDAYS[giga_birthsecond.weekday()]

    # time to be lived minus current date(which varies)
    days_left = (giga_birthsecond - date.today()).days

    # output
    print(anniversary, days_left, "days left")

# calling our function with a random variable
print(get_user_b_date(1991, 1, 24))
