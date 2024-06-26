from datetime import datetime
import pandas as pd

class Space:
    def __init__(self, id, description, price, user_id, name, fromdate, todate, free_dates=[]):
        self.id = id
        self.description = description
        self.price = price
        self.user_id = user_id
        self.name = name
        self.fromdate = fromdate
        self.todate = todate
        self.convertfrom = pd.to_datetime(fromdate, dayfirst=True).date()
        self.convertto = pd.to_datetime(todate, dayfirst=True).date()
        self.free_dates = pd.date_range(start=self.convertfrom,end=self.convertto)
        self.free_dates = list(self.free_dates.strftime('%d-%m-%Y'))


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Space({self.id}, {self.description}, {self.price}, {self.user_id}, {self.name}, {self.fromdate}, {self.todate}, {self.free_dates})'

