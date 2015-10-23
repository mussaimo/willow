# FEATURE PHONE KEY PRESSES
# LANGUAGE: PYTHON


# This is a feature phone keypad:

# ------- ------- -------
# |     | | ABC | | DEF |
# |  1  | |  2  | |  3  |
# ------- ------- -------
# ------- ------- -------
# | GHI | | JKL | | MNO |
# |  4  | |  5  | |  6  |
# ------- ------- -------
# ------- ------- -------
# |PQRS | | TUV | | WXYZ|
# |  7  | |  8  | |  9  |
# ------- ------- -------
# ------- ------- -------
# |     | |     | |     |
# |  *  | |  0  | |  #  |
# ------- ------- -------


<<<<<<< HEAD
# Before predictive text entry systems like T9, you had to press a button
# repeatedly to cycle through the possible values until you reached
# the one you wanted.

# For example, to type "V8" you would press the 8 key three times and then
# again four times (pressing the 8 key cycles through T->U->V->8),
# giving us a total of seven key presses.

# Note: the 0 key handles spaces and outputs 0 when tapped twice.

# Write a function that can calculate the amount of button presses required for
# any phrase. Except for spaces, punctuation can be ignored.
# Your function should accept both uppercase and lowercase letters
# and treat them the same.
=======
# Before predictive text entry systems like T9, you had to press a button repeatedly to cycle through the possible values until you reached the one you wanted.
# For example, to type "V8" you would press the 8 key three times and then
# again four times (pressing the 8 key cycles through T->U->V->8), giving
# us a total of seven key presses.

# Note: the 0 key handles spaces and outputs 0 when tapped twice.

# Write a function that can calculate the amount of button presses
# required for any phrase. Except for spaces, punctuation can be ignored.
# Your function should accept both uppercase and lowercase letters and
# treat them the same.
>>>>>>> e1e09342b550f52c74789669b097439f8513e5ca

# Examples:

# presses('V8') # 7
# presses('LOL') # 9
# presses('How R u 2day') # 23
# presses("i 8 2 Many mandazi 4 brekky") # 55

# Bonus: Try to avoid hard-coding the number of button presses for each letter!


<<<<<<< HEAD
def presses(str):
    # Your Code Here!
    cell = {"ADGEJMPTW": 1,
            "BCEHKNQUX": 2,
            "CFILORVY": 3,
            "SZ234568": 4,
            "79": 5}

    num = 0

    for x in str.upper():
        for key, values in cell.items():
            if x in key:
                num += values
    return num
print presses("V8")
=======
>>>>>>> e1e09342b550f52c74789669b097439f8513e5ca
