#!/usr/bin/env python3

import datetime
import pandas as pd
from datetime import date

URL = "https://raw.githubusercontent.com/richard512/Little-Big-Data/master/famous-birthdates.csv"
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
            print
          
    # Essentialy the same thing as the conditions above, it just prints 
    # different sentences with different arguments  
    if arg == "yet":
        if today == anniversary:
            print(f"It is snakes now")
        else:
            print(f"not yet snakeroo")

"""
The following class has famous people and their birthdays.
It returns whether the celebrity's birthday falls on Snake's anniversary. If not,
it returns how many days to the most recent one. It also returns a column describing the number
of days they could have potentially played the game since they were born.
"""
class snakeSensei:
    def __init__(self):
        self.data = pd.read_csv(URL,delimiter=" ")

    #sampling same as tutorial
    def random_sample(self,n):
        #cleaning up the data. 
        self.data = self.data[~self.data.birthDate.isna()]

        self.data = self.data.sample(n).reset_index(drop=True)

        self.data = self.data.loc[:, ["firstname", "lastname", "birthDate"]]
    

    def calculate_celebrity_could_play(self):
    
        self.data["Days_they_could've_played"] = "Not born yet"
        self.data["Anniversary?"] = "Nope"
        self.data["Days_to_nearest_Anniversary?"] = "Passed already :("
        for idx in self.data.index:
            bday = self.data.at[idx, "birthDate"]
            year, month, day = bday.strip().split("-")
            date = datetime.datetime(int(year), int(month), int(day))
            diff = datetime.datetime(2005, 1, 25) - date
            if date < datetime.datetime(2005, 1, 25):
                self.data.loc[idx, "Days_they_could've_played"] = diff.days 
            if date == datetime.datetime(2005, 1, 25):
                self.data.loc[idx, "Anniversary?"] = "OMG yes"
            
            anni_days = date - datetime.datetime(date.year, 1, 25) 
            if anni_days.days > 0:
                self.data.loc[idx,"Days_to_nearest_Anniversary?"] = int(anni_days.days)
    #instead of asking for a cmd line argument for size of sample, the program prompts the user
    def run(self):
        n = int(input("Please Enter a number: "))
        self.random_sample(n)
        self.calculate_celebrity_could_play()
        print(self.data)
    
if __name__ == "__main__":
    isit_snakes("yet")
    isit_snakes("today")
    p = snakeSensei()
    p.run()