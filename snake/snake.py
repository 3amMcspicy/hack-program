#!/usr/bin/env python3

import datetime
from datetime import date

"""
Functions of hello-world type code
Returns a Yes or No to confirm if the date today is 
the anniversary of the nokia snakes game release date (25th Jan). 
"""
def isit_snakes(arg):
    
    today = date.today()
    thisYear = datetime.datetime.today().year
    anniversary = datetime.datetime(thisYear, 1, 25)
    if arg == "today":
        if today == anniversary:
            print(f"yesssss")
        else:
            print(f"noooooooo")
    # Essentialy the same thing as the conditions above, it just prints 
    # different sentences with different arguments  
    if arg == "yet":
        if today == anniversary:
            print(f"It is snakes now")
        else:
            print(f"not yet snakeroo")

if __name__ == "__main__":
    isit_snakes("yet")
    isit_snakes("today")