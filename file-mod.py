'''
Dan P
File modifier
Change basic aspects of file
*Access time
*Modified time
*Etc
'''
import os
import time
from stat import *
from random import randint

class file_mod:
    SECOND = 1
    MINUTE = SECOND * 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24
    # Will need to consider 28, 29, 30, 31
    # 30 for now...
    MONTH = DAY * 30
    # Will need to consider leap years...
    YEAR = DAY * 365

    def __init__(self, file):
        self.file = os.stat(file)
        self.time = self.file[ST_MTIME]


    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def add_seconds(self, seconds):
        self.time += seconds

    def remove_seconds(self, seconds):
        self.time -= seconds

    def add_minutes(self, minutes):
        self.time += (minutes * MINUTE)

    def remove_minutes(self, minutes):
        self.time -= (minutes * MINUTE)

    def add_hours(self, hours):
        self.time += int(hours * 3600)

    def remove_hours(self, hours):
        self.time -= hours * 3600

    def add_days(self, days):
        self.time += (days * DAY)

    def remove_days(self, days):
        self.time -= (days * DAY)

    def add_years(self, years):
        self.time += (years * YEAR)

    def remove_years(self, years):
        self.time -= (years * YEAR)

    def deploy(self, time):
        os.utime(self.file, (self.time, self.time))

def main():  
    # Files in current directory...
    files = os.listdir('.')

    for f in files:
        modz = file_mod(f)
        print modz.get_time()




if __name__ == "__main__":
    main()
