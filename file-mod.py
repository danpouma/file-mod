'''
Dan P

File modifier

Change basic aspects of file
'''
import os
from datetime import datetime
from stat import *

class file_mod:
    SECOND = 1
    MINUTE = SECOND * 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24
    
    # Use datetime to deterime correct days
    # based on month.
    MONTH = DAY * 30
    
    # Use datetime to determine correct days
    # in year based on leap years.
    YEAR = DAY * 365

    # Constructor
    def __init__(self, file):
        # Fie to mod
        self.file = os.stat(file)

        # Time of last access
        self.atime = self.file[ST_ATIME]

        #Time of last modification
        self.mtime = self.file[ST_MTIME]

    # Accessors
    def get_mtime(self):
        return self.mtime

    def get_atime(self):
        return self.atime

    # Modification mutators
    def set_mtime(self, mtime):
        self.mtime = mtime

    def add_seconds_mtime(self, seconds):
        self.mtime += seconds
        
    def add_minutes_mtime(self, minutes):
        self.mtime += (minutes * MINUTE)

    def add_hours_mtime(self, hours):
        self.mtime += (hours * HOUR)

    def add_days_mtime(self, days):
        self.mtime += (days * DAY)

    def add_months_mtime(self, months):
        self.mtime += (months * MONTH)

    def add_years_mtime(self, years):
        self.mtime += (years * YEAR)

    def remove_seconds_mtime(self, seconds):
        self.mtime -= seconds
        
    def remove_minutes_mtime(self, minutes):
        self.mtime -= (minutes * MINUTE)

    def remove_hours_mtime(self, hours):
        self.mtime -= (hours * HOUR)

    def remove_days_mtime(self, days):
        self.mtime -= (days * DAY)

    def remove_months_mtime(self, months):
        self.mtime -= (months * MONTH)

    def remove_years_mtime(self, years):
        self.mtime -= (years * YEAR)


    # Accesor mutators
    def set_atime(self, atime):
        self.atime = atime
        
    def add_seconds_atime(self, seconds):
        self.atime += seconds
        
    def add_minutes_atime(self, minutes):
        self.atime += (minutes * MINUTE)

    def add_hours_atime(self, hours):
        self.atime += (hours * HOUR)

    def add_days_atime(self, days):
        self.atime += (days * DAY)

    def add_months_atime(self, months):
        self.atime += (months * MONTH)

    def add_years_atime(self, years):
        self.atime += (years * YEAR)
        
    def remove_seconds_atime(self, seconds):
        self.atime -= seconds
        
    def remove_minutes_atime(self, minutes):
        self.atime -= (minutes * MINUTE)

    def remove_hours_atime(self, hours):
        self.atime -= (hours * HOUR)

    def remove_days_atime(self, days):
        self.atime -= (days * DAY)

    def remove_months_atime(self, months):
        self.atime -= (months * MONTH)

    def remove_years_atime(self, years):
        self.atime -= (years * YEAR)

    # Will this needs parameters?
    # double check...
    def deploy(self):
        # This is what changes the file
        # based on access and modification times
        os.utime(self.file, (self.acess, self.modification))

# This is a test function to display the ticks
# as a date using datetime module
# *** Can throw this into class for even more capability!
def ticks_to_date(ticks):
    return datetime.fromtimestamp(ticks)


def main():  
    # Files in current directory...
    files = os.listdir('.')

    for f in files:
        modz = file_mod(f)
        print modz.get_mtime()
        print tick_to_date(modz.get_mtime())

if __name__ == "__main__":
    main()
