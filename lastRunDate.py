#This file is no longer used. program points to external lastRun.py
class LastRunDate:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return self.date
    
    def set(self, date):
        assert isinstance(date, str)
        self.date = date

lastRunDat = LastRunDate("2024-04-25")